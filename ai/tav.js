const { tavily } = require("@tavily/core");

const tvly = tavily({ apiKey: "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" });

async function main() {
  const response = await tvly.search("search git hub of harshad200 ");
  console.log(response);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});