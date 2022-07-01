// server.js
// where your node app starts

// init project
var express = require("express");
var app = express();

// enable CORS (https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)
// so that your API is remotely testable by FCC
var cors = require("cors");
app.use(cors({ optionsSuccessStatus: 200 })); // some legacy browsers choke on 204

// http://expressjs.com/en/starter/static-files.html
app.use(express.static("public"));

// http://expressjs.com/en/starter/basic-routing.html
app.get("/", function (req, res) {
  res.sendFile(__dirname + "/views/index.html");
});

// your first API endpoint...
app.get("/api/hello", function (req, res) {
  res.json({ greeting: "hello API" });
});

app.get("/api/timestamp/:date?", (req, res) => {
  const regex = /^[0-9]{4}-[0-9]{2}-[0-9]{2}$/;
  const regex2 = /^[0-9]+$/;
  const curr = new Date(Date.now());
  if (req.params.date) {
    const date = req.params.date;

    if (date.match(regex)) {
      const obj = {
        year: parseInt(date.split("-")[0]),
        month: parseInt(date.split("-")[1]) - 1,
        day: parseInt(date.split("-")[2]),
      };
      const readyDate = new Date(obj.year, obj.month, obj.day);
      return res.json({
        utc: readyDate.toUTCString(),
        unix: readyDate.valueOf(),
      });
    } else if (date.match(regex2)) {
      console.log(parseInt(date));
      const readyDate = new Date(parseInt(date));
      return res.json({
        utc: readyDate.toUTCString(),
        unix: readyDate.valueOf(),
      });
    }
    const test = new Date(date);
    console.log(test);
    if (test.valueOf()) {
      console.log("here string");
      return res.json({
        utc: test.toUTCString(),
        unix: test.valueOf(),
      });
    }

    return res.json({ error: "Invalid Date" });
  }
  return res.json({
    utc: curr.toUTCString(),
    unix: curr.valueOf(),
  });
});

// listen for requests :)
var listener = app.listen(process.env.PORT, function () {
  console.log("Your app is listening on port " + listener.address().port);
});
