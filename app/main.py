from nlplot import server

# Generate the plot
plot = nlplot.line(x=[1, 2, 3], y=[4, 5, 6])

# Start the server
server.start(plot)

