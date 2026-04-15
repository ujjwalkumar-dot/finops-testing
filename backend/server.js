const express = require("express");
const { exec } = require("child_process");
const cors = require("cors");
const { scripts } = require("../scripts");

const app = express();
app.use(cors());
app.use(express.json());

// CONFIG DRIVEN SCRIPTS


// GET ALL SCRIPTS
app.get("/scripts", (req, res) => {
  res.json(scripts);
});

// RUN SCRIPT
app.post("/run", (req, res) => {
  const { command, cwd } = req.body;

  exec(command, { cwd }, (error, stdout, stderr) => {
    if (error) {
      return res.json({
        success: false,
        output: stderr || error.message
      });
    }

    res.json({
      success: true,
      output: stdout
    });
  });
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});