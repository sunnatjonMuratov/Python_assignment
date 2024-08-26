def generate_reservation_page(reservations):
    html = """<html>
    <head>
        <title>Reservations</title>
        <link rel="stylesheet" type="text/css" href="styles.css">
    </head>
    <body>
        <header>
            <h1>Restaurant Reservation System</h1>
            <div id="current-time"></div>
        </header>
        <main>
            <h2>Make a Reservation</h2>
            <form id="reservation-form" action="/add_reservation" method="post">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name">
                <label for="date">Date:</label>
                <input type="date" id="date" name="date">
                <label for="time">Time:</label>
                <input type="time" id="time" name="time">
                <label for="guests">Number of Guests:</label>
                <input type="number" id="guests" name="guests" min="1">
                <button type="submit">Reserve</button>
            </form>

            <h2>Current Reservations</h2>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Date</th>
                    <th>Time</th>
                    <th>Guests</th>
                </tr>"""
# dadadadda


# dada
    for res in reservations:
        html += f"<tr><td>{res[0]}</td><td>{res[1]}</td><td>{res[2]}</td><td>{res[3]}</td></tr>"

    html += """</table>
        </main>
        <script src="script.js"></script>
    </body>
    </html>"""

    return html
