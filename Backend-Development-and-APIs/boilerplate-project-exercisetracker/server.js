const express = require("express");
const app = express();
const cors = require("cors");
const mongoose = require("mongoose");
require("dotenv").config();
// models
const User = require("./models/user");
const Exercise = require("./models/exercise");
//helpers
const { validateMongoObjectId, validateDate } = require("./helpers");

const main = async () => {
  try {
    await mongoose.connect(process.env.MONGO_URL, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
      useCreateIndex: true,
    });
  } catch (err) {
    console.log(err);
  }
  app.use(cors());
  app.use(express.urlencoded({ extended: true }));
  app.use(express.static("public"));
  app.get("/", (req, res) => {
    res.sendFile(__dirname + "/views/index.html");
  });
  app.post("/api/users", async (req, res) => {
    const { username: newUsername } = req.body;
    if (!newUsername) {
      return res.status(400).json({
        ok: false,
        message: "Please provide a username",
      });
    }
    const duplicate = await User.findOne({
      username: newUsername,
    });
    if (duplicate) {
      return res.status(400).json({
        ok: false,
        message: "Username already taken",
      });
    }
    const userCreated = await User.create({
      username: newUsername,
    });
    return res.status(200).json(userCreated);
  });

  app.post("/api/users/:_id/exercises", async (req, res) => {
    let { description, duration, date } = req.body;
    if (!description || !duration) {
      return res.status(400).json({
        ok: false,
        message: "Description and duration are required",
      });
    }
    if (Number.isNaN(Number(duration))) {
      return res.status(400).json({
        ok: false,
        message: "Invalid Duration",
      });
    }
    duration = Number(duration);
    if (!date) {
      date = new Date();
    } else if (!validateDate(date)) {
      return res.status(400).json({
        ok: false,
        message: "Invalid Date",
      });
    }
    date = new Date(date);
    const { _id: userId } = req.params;
    if (!validateMongoObjectId(userId)) {
      return res.status(400).json({
        ok: false,
        message: "Invalid User id",
      });
    }
    const user = await User.findById(userId);
    if (!user) {
      return res.status(404).json({
        ok: false,
        message: "User not found",
      });
    }
    try {
      const exercise = await Exercise.create({
        user: new mongoose.mongo.ObjectId(userId),
        description,
        duration,
        date,
      });
    } catch (err) {
      console.log(err);
      return res.status(500).json(err);
    }

    return res.status(200).json({
      _id: userId,
      username: user.username,
      date: date.toDateString(),
      duration,
      description,
    });
  });

  app.get("/api/users", async (req, res) => {
    const users = await User.find({});
    return res.json(users);
  });

  app.get("/api/users/:_id/logs", async (req, res) => {
    let { limit, from, to } = req.query;
    if (from) {
      if (!validateDate(from)) {
        return res.status(400).json({
          ok: false,
          message: "Invalid from date",
        });
      }
    }
    if (to) {
      if (!validateDate(to)) {
        return res.status(400).json({
          ok: false,
          message: "Invalid to date",
        });
      }
    }

    const { _id: userId } = req.params;
    if (!validateMongoObjectId(userId)) {
      return res.status(400).json({
        ok: false,
        message: "Invalid User id",
      });
    }
    const user = await User.findById(userId);
    if (!user) {
      return res.status(404).json({
        ok: false,
        message: "User not found",
      });
    }
    if (Number.isNaN(Number(limit))) {
      limit = undefined;
    } else {
      limit = Number(limit);
    }
    const queryObj = {
      user: new mongoose.mongo.ObjectId(userId),
    };
    if (from || to) {
      queryObj["date"] = {};
      if (from) {
        queryObj.date["$gte"] = new Date(from);
      }
      if (to) {
        queryObj.date["$lte"] = new Date(to);
      }
    }
    let exercises;
    try {
      exercises = await Exercise.find(queryObj).limit(limit);
    } catch (err) {
      return res.json(err);
    }

    return res.status(200).json({
      _id: userId,
      username: user.username,
      count: exercises.length,
      log: exercises.map((exercise) => ({
        description: exercise.description,
        duration: exercise.duration,
        date: exercise.date.toDateString(),
      })),
    });
  });

  const listener = app.listen(process.env.PORT || 4000, () => {
    console.log("Your app is listening on port " + listener.address().port);
  });
};
main();
