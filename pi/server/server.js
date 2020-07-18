const express = require("express")
const bodyParser = require('body-parser')
const sql = require('sqlite3').verbose()
const { exec } = require('child_process')

// Open the database connection
let db = new sql.Database('./db_files/daq.db', (err) => { console.log("Database connection error: ", err) })

// Load Express
const app = express()
const port = 5000;

app.use(bodyParser.json())

// Middleware to allow static paths to serve files
app.use(express.static('views'));

// Function to get current logging status
getLoggingStatus = () => { return true }

// --------------------------------------------------------------------
// Get Request Handlers for Page Loading
// --------------------------------------------------------------------

// Redirect to the route /home
app.get('/', (req, res) => { res.redirect('/home') })

// Serve home page
app.get('/home', (req, res) => {
    res.send('home.html')
})

// Serve downloads page
app.get('/log-history', (req, res_) => {
    if (!getLoggingStatus()) { res.send('logs.html') }
    else { res.sendStatus(403).send('<h1>403 Forbidden: disable logging to download files</h1>') }
})

// --------------------------------------------------------------------
// Get request handler for serving downloads
// --------------------------------------------------------------------

app.get('/download/log/:id', (req, res) => {
    if (!getLoggingStatus()) { res.download(`../logs/${req.params.id}.csv`) }
    else { res.sendStatus(403).send('<h1>403 Forbidden: disable logging to download files</h1>') }
})

// --------------------------------------------------------------------
// Post request handlers for serving/receiving data
// --------------------------------------------------------------------

app.post('/get-calibration', (req,res)=> {

    // Initialize output object
    var calibration

    // TODO get calibration parameters and loop over them, pushing them to the object

    res.JSON(calibration)

})

app.post('/set-calibration', (req, res) => {

    // Parse JSON
    const surveyData = JSON.parse(req.body.data)



})

// Return list of log files
app.post('/enum-logs', (req, res) => {

    if (getLoggingStatus()) {
        // Get data and return it
        /* 
        Array of objects with properties:
        - name
        - duration
        - downloadLink
        */
    }
    else {
        res.JSON({
            "message": "Error: cannot get logs while system is acquiring data. Stop Acquisition to access log history."
        })
    }

})

// --------------------------------------------------------------------
// Get request handler to shutdown the system
// --------------------------------------------------------------------

app.get('/powerctl/:mode', (req, res) => {

    // Close the database connection
    db.close((err) => {
        // If there's an error, log it to the console
        if (err) { console.log(err) }

        // Resistance is futile. The system is still going to shutdown
        switch (mode) {
            case "shutdown": {
                exec("shutdown +1")
                break
            }
            case "restart": {
                exec("shutdown -r +1")
                break
            }
        }
        // Exit Node
        process.exit(0)
    })

})

// --------------------------------------------------------------------

app.listen(port, () => { console.log(`Listening on port ${port}`) })