require("dotenv").config();
const express = require("express");
const cors = require("cors");
const app = express();
const mongoose = require("mongoose");
const { Url } = require("./models/url");

const main = async () => {
  try {
    await mongoose.connect(process.env.DB_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
  } catch (err) {
    console.log(err);
  }
  // Basic Configuration
  const port = process.env.PORT || 3000;

  app.use(cors());

  app.use("/public", express.static(`${process.cwd()}/public`));

  app.get("/", function (req, res) {
    res.sendFile(process.cwd() + "/views/index.html");
  });

  // Your first API endpoint
  app.get("/api/hello", function (req, res) {
    res.json({ greeting: "hello API" });
  });
  app.use(express.urlencoded({ extended: true }));
  app.post("/api/shorturl/new", async (req, res) => {
    const regex = /^https?:\/\/[^(\.)]+\.[^(\.)]+/;
    const tester = regex.test(req.body.url);
    if (!tester) {
      return res.json({ error: "invalid url" });
    }
    let url = await Url.findOne({ original_url: req.body.url }).exec();
    if (url) {
      console.log("that url already exists");
      return res.json({
        original_url: url.original_url,
        short_url: url.short_url,
      });
    }
    let maxUrl = null;

    const urls = await Url.find().sort({ short_url: -1 }).exec();
    if (Array.isArray(urls)) {
      if (urls.length > 0) {
        // There is at least one url
        maxUrl = urls[0];
      }
    }
    if (maxUrl) {
      url = await Url.create({
        original_url: req.body.url,
        short_url:
          typeof maxUrl.short_url === "number"
            ? maxUrl.short_url + 1
            : Math.floor(Math.random() * Math.floor(99999999999999999)),
      });
    } else {
      // there is no urls
      url = await Url.create({ original_url: req.body.url, short_url: 1 });
    }

    console.log(url);
    if (!url) {
      return res.status(500).json({ error: "error de servidor" });
    }
    url = { original_url: url.original_url, short_url: url.short_url };
    return res.json(url);
  });
  app.get("/api/shorturl/:original_url", async (req, res) => {
    const url = await Url.findOne({
      short_url: req.params.original_url,
    }).exec();
    console.log(url);
    if (!url) {
      return res.json({ error: "invalid url" });
    }

    return res.redirect(url.original_url);
  });
  app.listen(port, function () {
    console.log(`Listening on port ${port}`);
  });
};
main();
