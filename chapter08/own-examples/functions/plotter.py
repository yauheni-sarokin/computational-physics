def plot(xp: [], yp: [], title='graph'):
    from vpython import graph, gcurve, color
    graph1 = graph(width=400, height=400, title='<b>RK4</b>', xtitle='<i>t</i>',
                   ytitle='<i>Y[0]</i><sup>2</sup>')
    funct1 = gcurve(color=color.blue)
    graph1.title = title
    for x, y in zip(xp, yp):
        funct1.plot(x, y)
