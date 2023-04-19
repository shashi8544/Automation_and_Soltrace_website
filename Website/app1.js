// define mongoose and give path to your database
const express = require("express");
const path = require("path");
const fs = require("fs");
const bodyParser = require('body-parser')
const app = express();
const port = process.env.PORT || 3000;
const hostname = '127.0.0.1';
var hbs  = require('hbs');
app.use(bodyParser.urlencoded({ extended: false }))
app.use(express.static(__dirname + '/public'));
// parse application/json
app.use(bodyParser.json())
// require("E:\\web_devlopment\\backend\\soltrace_tut\\db\\conn.js")
const solds = require('./app')
// const static_path = path.join(__dirname,'views')
const template_path = path.join(__dirname,'./template/views')
const partials_path = path.join(__dirname,'./template/partials')
console.log(path.join(__dirname,'./template/partials'))
// app.use(express.static(static_path))

// app.engine('.hbs', exphbs({extname: '.hbs'}));
app.set('view engine', 'hbs');
app.set("views",template_path);
hbs.registerPartials(partials_path)
app.get("/",(req,res)=>{
    res.render("index")
})
app.get("/Soltrace",(req,res)=>{
    res.render("soltrace")
})
app.get("/Input",(req,res)=>{
    res.render("Input")
})
app.get("/result",(req,res)=>{
    res.render("result")
})


const getDocument = async (req, res) =>{
  try{
  //const res = await solds.find();
  // console.log(req, req.body);
  var sunpos1 = req.body.sunposa;
  //var R_App_g11 = req.body.R_App_g1;
  var rappdia11 = req.body.rappdia1;

  // const {sunposa, R_App_g1, rappdia1} = req.body;

  var R_Surf_g11 = req.body.R_Surf_g1;
  var recsurfdiaC11 = req.body.recsurfdiaC1;
  var recsurfdiaC21 = req.body.recsurfdiaC2;
  //var C_App_geom11 = req.body.C_App_geom1;
  var cappgeom11 = req.body.cappgeom1;
  console.log("here passing value of sunpos "+sunpos1);
  console.log("here passing value of sunpos "+R_Surf_g11);
  // const res1 = await solds.find({R_Surf_geom:'p'})
  const res1 = await solds.find({Angle : sunpos1,R_App_dia:rappdia11,R_Surf_geom:R_Surf_g11,R_Surf_C1:recsurfdiaC11,C_Pos_Z:recsurfdiaC21,C_App_dia:cappgeom11})
      // .select({Avg_Flux:1})
  res.status(200).json({
    status : "success",
    data : res1,
  });
  }catch(err){
    res.status(500).json({
      status : "error",
    });
      console.log(err);
  }
}
app.post("/getdata", getDocument);
app.get("/getdata", getDocument);
// new user in database

// app.get("/",(req,res)=>{
//     res.send("hey welcome back")
// })

app.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
  });
