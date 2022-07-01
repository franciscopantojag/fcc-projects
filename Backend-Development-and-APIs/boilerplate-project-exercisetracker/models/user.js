const mongoose = require("mongoose");

const { model, Schema } = mongoose;

const userSchema = new Schema({
  username: {
    type: String,
    unique: true,
    required: true,
  },
});

const User = model("User", userSchema);
module.exports = User;
