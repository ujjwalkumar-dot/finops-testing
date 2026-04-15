const express = require("express");
const { exec } = require("child_process");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// CONFIG DRIVEN SCRIPTS
const scripts ={
  pipeline:{
    scripts: [
  {
    id: "REG-001",
    name: "Regression 001",
    command: "npm run REG-001",
    description:"This is used to create pipeline",
    cwd: "../reconciliation-tests"
  },
  {
    id: "REG-002",
    name: "Regression 002",
    command: "npm run REG-002",
    cwd: "../reconciliation-tests"
  },
  {
    id: "REG-003",
    name: "Regression 003",
    command: "npm run REG-003",
    cwd: "../reconciliation-tests"
  }
]
  },
  reference:{
        scripts: [
  {
    id: "REG-006",
    name: "Regression 006",
    command: "npm run REG-001",
    description:"This is used to create pipeline",
    cwd: "../reconciliation-tests"
  },]
  }
};

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

app.listen(5000, () => {
  console.log("Server running on port 5000");
});