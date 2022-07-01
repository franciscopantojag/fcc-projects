const mongoose = require('mongoose');

const Url = mongoose.model("Url", {
  original_url: {
    type: String,
    required: true
    },
  short_url: {
    type: Number,
    required: true
    }
})

exports.Url = Url