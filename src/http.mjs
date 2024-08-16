"use strict";

import http from "node:http";

const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/html" });
  res.end(
    "<html><head><title>http.js</title></head><body><h1>Hello World</h1></body></html>"
  );
});

console.log("Server started on port 9000");
server.listen(9000);

process.on("SIGINT", () => {
  console.log("\nShutting down\n");
  server.close();
});
