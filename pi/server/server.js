const express = require("express")
const bodyParser = require('body-parser')

// Load Express
const app = express()
const port = 5000;

app.use(bodyParser.json())

// Middleware to allow static paths to serve files
app.use(express.static('views'));

// --------------------------------------------------------------------
// Get Request Handlers for Page Loading
// --------------------------------------------------------------------

// Redirect to the route /home
app.get('/',(req,res)=>{res.redirect('/home')})

// Serve home page
app.get('/home',(req,res)=>{
    res.send('home.html')
})

// --------------------------------------------------------------------
// Post request handlers for serving data
// --------------------------------------------------------------------

app.post()