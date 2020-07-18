

initLogs = () => {
    $.get('/enum-logs', data => {
        var logList = document.getElementById("logList")

        data.forEach(log => {

            // Create card
            var logEl = document.createElement("div")
            logEl.className = "card"

            // Create card header
            var cardHeader = document.createElement("div")
            cardHeader.className = "card-header"
            cardHeader.innerHTML = log.name
            logEl.appendChild(cardHeader)
            // Create Download button
            var downloadButton = document.createElement("a")
            downloadButton.href = log.downloadLink
            downloadButton.classList.add("btn")
            downloadButton.classList.add("btn-info")
            cardBody.appendChild(downloadButton)

            // Create card body
            var cardBody = document.createElement("div")
            cardBody.className = "card-body"
            cardBody.innerHTML = `Recording duration: ${log.duration}`
            logEl.appendChild(cardBody)

        });
    })
}