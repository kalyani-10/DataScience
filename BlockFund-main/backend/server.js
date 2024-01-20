const app       = require("./routes/router");
const http      = require("http");
const mongoose  = require("mongoose");


// MongoDB connection
const hostname = '192.168.0.131';
const port = 3000;
mongoose.connect("mongodb+srv://keyurkolambe:qwerty0987@cluster0.s0j1it6.mongodb.net/?retryWrites=true&w=majority",
{ useNewUrlParser: true,
  useCreateIndex:true,
  useFindAndModify:false,
  useUnifiedTopology: true
}).then(() => {
    console.log("Connected to MongoDB");
}).catch(err => {
    console.log("Error connecting to Collective Database",err.message);
});



// Server setup

const server = http.createServer(app);

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}`);
});
