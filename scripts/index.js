export const scripts = {
  pipeline: {
    scripts: [
      {
        id: "REG-001",
        name: "Create pipeline with valid data",
        command: "npm run REG-001",
        cwd: "../reconciliation-tests",
        description: "Create pipeline with valid data"
      },
      {
        id: "REG-002",
        name: "Create pipeline with missing mandatory fields",
        command: "npm run REG-002",
        cwd: "../reconciliation-tests",
        description: "Validate missing mandatory fields during pipeline creation"
      },
      {
        id: "REG-003",
        name: "Upload single valid file",
        command: "npm run REG-003",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-004",
        name: "Upload multiple files",
        command: "npm run REG-004",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-005",
        name: "Create reference table",
        command: "npm run REG-005",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-008",
        name: "Assign field types",
        command: "npm run REG-008",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-009",
        name: "Change field type",
        command: "npm run REG-009",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-010",
        name: "Mandatory Amount & Currency validation",
        command: "npm run REG-010",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-011",
        name: "Auto mapping (Smart Match)",
        command: "npm run REG-011",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-012",
        name: "Manual mapping",
        command: "npm run REG-012",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-013",
        name: "Delete mapping",
        command: "npm run REG-013",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-014",
        name: "Mapping validation",
        command: "npm run REG-014",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-015",
        name: "Mandatory rule enforcement",
        command: "npm run REG-015",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-016",
        name: "Optional rule behavior",
        command: "npm run REG-016",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-017",
        name: "Ignore rule behavior",
        command: "npm run REG-017",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-018",
        name: "Rule removal",
        command: "npm run REG-018",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-019",
        name: "Create rule set",
        command: "npm run REG-019",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-020",
        name: "Delete rule set",
        command: "npm run REG-020",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-025",
        name: "Run matching",
        command: "npm run REG-025",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-047",
        name: "Full pipeline flow",
        command: "npm run REG-047",
        cwd: "../reconciliation-tests"
      }
    ]
  },
  "Data Upload": {
    scripts: [
      {
        id: "REG-050",
        name: "Upload valid file (CSV/XLSX)",
        command: "npm run REG-050",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-051",
        name: "Upload multiple valid files",
        command: "npm run REG-051",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-052",
        name: "File type mismatch",
        command: "npm run REG-052",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-053",
        name: "Unsupported file type",
        command: "npm run REG-053",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-054",
        name: "File size limit exceeded",
        command: "npm run REG-054",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-055",
        name: "Partial upload failure handling",
        command: "npm run REG-055",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-056",
        name: "File consistency (same schema)",
        command: "npm run REG-056",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-057",
        name: "File inconsistency (different schema)",
        command: "npm run REG-057",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-058",
        name: "File inconsistency (data type mismatch)",
        command: "npm run REG-058",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-059",
        name: "Missing headers",
        command: "npm run REG-059",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-060",
        name: "Large dataset handling (>1000 rows)",
        command: "npm run REG-060",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-061",
        name: "Delete single file",
        command: "npm run REG-061",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-062",
        name: "Delete all files (bulk)",
        command: "npm run REG-062",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-063",
        name: "Delete during upload",
        command: "npm run REG-063",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-064",
        name: "Re-upload after delete",
        command: "npm run REG-064",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-065",
        name: "Upload status handling",
        command: "npm run REG-065",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-066",
        name: "Error message clarity",
        command: "npm run REG-066",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-067",
        name: "Multiple file errors handling",
        command: "npm run REG-067",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-068",
        name: "Duplicate file upload",
        command: "npm run REG-068",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-069",
        name: "Network failure during upload",
        command: "npm run REG-069",
        cwd: "../reconciliation-tests"
      }
    ]
  },
  reference: {
    scripts: [
      {
        id: "REG-005",
        name: "Create reference table",
        command: "npm run REG-005",
        cwd: "../reconciliation-tests",
        description: "Create and validate reference table"
      }
    ]
  },

 

  DPP: {
    scripts: [
      {
        id: "REG-036",
        name: "Exception generation",
        command: "npm run REG-036",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-037",
        name: "Resolve exception",
        command: "npm run REG-037",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-040",
        name: "Export data",
        command: "npm run REG-040",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-045",
        name: "Access restriction",
        command: "npm run REG-045",
        cwd: "../reconciliation-tests"
      },
      {
        id: "REG-046",
        name: "Large dataset handling",
        command: "npm run REG-046",
        cwd: "../reconciliation-tests"
      }
    ]
  }
};
