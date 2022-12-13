// Imports
const fs = require("fs");
const reader = require("readline-sync");

// User Input
const name = reader.question("Component name: ");
const subDirectory = reader.question("Subdirectory [Optional]: ");

// File Content
const directoryCount = subDirectory ? subDirectory.split("/").length : 0;

const content = `<!-- ${name}.svelte -->
<script lang="ts">
  // Add TypeScript Here ...
</script>
<!-- Add HTML Here ... -->
<style lang="scss">
  @import "${"../".repeat(directoryCount)}../styles/style.scss";
  // Add SCSS Here ...
</style>
`;

// Create File
const directory = `./src/components/${subDirectory ? `/${subDirectory}/` : ""}`
let filepath = `${directory}${name}.svelte`;

if (fs.existsSync(filepath)) {
  throw new Error(`Failed! Component ${filepath} already exists!`)
}
if (!fs.existsSync(directory)) {
  fs.mkdirSync(directory, { recursive: true })
}
fs.writeFile(filepath, content, function (err) {
  if (err) throw err;
  console.log(`\nSuccess!\n+ ${name}`);
});
