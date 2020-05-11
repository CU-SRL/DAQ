var temperatureChart
var forceChart
var pressureChart

initCharts = () => {

    // Get canvas elements
    var temperatureCanvas = document.getElementById('temperatureCanvas').getContext('2d');
    var forceCanvas = document.getElementById('forceCanvas').getContext('2d');
    var pressureCanvas = document.getElementById('pressureCanvas').getContext('2d');

    // Init data
    var temperatureConfig = {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            datasets: [{
                label: 'Thermocouple 1',
                backgroundColor: 'rgb(0,0,0,0)',
                borderColor: 'rgb(255, 99, 132)',
                data: [{
                    x: 0,
                    y: 5
                }, {
                    x: 1,
                    y: 10
                }, {
                    x: 2,
                    y: 15
                }, {
                    x: 3,
                    y: 20
                }]
            },
            {
                label: 'Thermocouple 2',
                backgroundColor: 'rgb(0,0,0,0)',
                borderColor: 'rgb(58, 157, 214)',
                data: [{
                    x: 0,
                    y: 6
                }, {
                    x: 1,
                    y: 11
                }, {
                    x: 2,
                    y: 16
                }, {
                    x: 3,
                    y: 21
                }]
            },
            {
                label: 'Thermocouple 3',
                backgroundColor: 'rgb(0,0,0,0)',
                borderColor: 'rgb(255, 145, 0)',
                data: [{
                    x: 0,
                    y: 7
                }, {
                    x: 1,
                    y: 12
                }, {
                    x: 2,
                    y: 17
                }, {
                    x: 3,
                    y: 22
                }]
            }]
        },

        // Configuration options go here
        options: {
            scales: {
                xAxes: [{
                    type: 'linear',
                    position: 'bottom'
                }]
            }
        }
    };
    var forceConfig = {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            datasets: [{
                label: 'Load Cell',
                backgroundColor: 'rgb(0,0,0,0)',
                borderColor: 'rgb(255, 99, 132)',
                data: [{
                    x: 0,
                    y: 5
                }, {
                    x: 1,
                    y: 10
                }, {
                    x: 2,
                    y: 20
                }, {
                    x: 3,
                    y: 40
                }]
            }]
        },

        // Configuration options go here
        options: {
            scales: {
                xAxes: [{
                    type: 'linear',
                    position: 'bottom'
                }]
            }
        }
    };
    var pressureConfig = {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            datasets: [{
                label: 'Transducer 1',
                backgroundColor: 'rgb(0,0,0,0)',
                borderColor: 'rgb(255, 99, 132)',
                data: [{
                    x: 0,
                    y: 5
                }, {
                    x: 1,
                    y: 10
                }, {
                    x: 2,
                    y: 15
                }, {
                    x: 3,
                    y: 20
                }]
            },
            {
                label: 'Transducer 2',
                backgroundColor: 'rgb(0,0,0,0)',
                borderColor: 'rgb(58, 157, 214)',
                data: [{
                    x: 0,
                    y: 6
                }, {
                    x: 1,
                    y: 11
                }, {
                    x: 2,
                    y: 16
                }, {
                    x: 3,
                    y: 21
                }]
            },
            {
                label: 'Transducer 3',
                backgroundColor: 'rgb(0,0,0,0)',
                borderColor: 'rgb(255, 145, 0)',
                data: [{
                    x: 0,
                    y: 7
                }, {
                    x: 1,
                    y: 12
                }, {
                    x: 2,
                    y: 17
                }, {
                    x: 3,
                    y: 22
                }]
            }]
        },

        // Configuration options go here
        options: {
            scales: {
                xAxes: [{
                    type: 'linear',
                    position: 'bottom'
                }]
            }
        }
    };

    temperatureChart = new Chart(temperatureCanvas, temperatureConfig);
    forceChart = new Chart(forceCanvas, forceConfig);
    pressureChart = new Chart(pressureCanvas, pressureConfig);
}

pushTemperature = (t,T) => {
    temperatureChart.data.datasets.forEach((dataset,idx) => {
        dataset.data.push({
            x: t[idx],
            y: T[idx]
        })
    })
}

updateTemperature = () => {temperatureChart.update()}

pushPressure = (t,P) => {
    pressureChart.data.datasets.forEach((dataset,idx) => {
        dataset.data.push({
            x: t[idx],
            y: P[idx]
        })
    })
}

updatePressure = () => {pressureChart.update()}

pushForce = (t,F) => {
    forceChart.data.datasets[0].data.push({
        x: t,
        y: F
    })
}

updateForce = () => {forceChart.update()}