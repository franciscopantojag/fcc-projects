const mongoose = require("mongoose");

const { model, Schema } = mongoose;

const exerciseSchema = new Schema({
  user: {
    type: Schema.Types.ObjectId,
    required: true,
    ref: "User",
  },
  description: {
    type: String,
    required: true,
  },
  duration: {
    type: Number,
    required: true,
  },
  date: Date,
});

const Exercise = model("Exercise", exerciseSchema);
module.exports = Exercise;
