var width = 400;
var height = 400;
var radius = Math.min(width, height) / 2;
var donutWidth = 75;

var color = d3.scaleOrdinal()
// color order: negative, positive, neutral
.range(["#FF3232", "#3CB371", "#7B60BC"]);

var svg = d3.select('#donut')
    .append('svg')
    .attr('width', width)
    .attr('height', height)
    .append('g')
    .attr('transform', 'translate(' + (width / 2) + ',' + (height / 2) + ')');

var arc = d3.arc()
    .innerRadius(radius - donutWidth)
    .outerRadius(radius);

var pie = d3.pie()
    .value(function (d) {
        return d.value;
    })
    .sort(null);

var div = d3.select("body").append("div")
    .attr("class", "tooltip-donut")
    .style("opacity", 0);

d3.queue()
    .defer(d3.json, "testD3Resultpi.json")
    .await(ready)

function ready (error, datapoints) {
    var path = svg.selectAll('path')
        .data(pie(datapoints))
        .enter()
        .append('path')
        .attr('d', arc)
        .attr('fill', function(d, i) {
            return color(d.data[0]);
        })
        .attr('transform', 'translate(0,0)')

        // hover effects
        .on('mouseover', function(d, i) {
            d3.select(this).transition()
                .duration('50')
                .attr('opacity', '0.65');
            
            // Values appear on hover
            div.transition()
                .duration('50')
                .style("opacity", 1);
            
            let num = (Math.round((d.value / 1038) * 100)).toString() + '%';

            div.html(num)
                .style("left", (d3.event.pageX + 10) + "px")
                .style("top", (d3.event.pageY - 15) + "px");
        })

    .on('mouseout', function(d, i) {
        d3.select(this).transition()
            .duration('50')
            .attr('opacity', '1');
        
        // Values disappear
        div.transition()
            .duration('50')
            .style("opacity", 0);
    });

    // Legend
    var legendRectSize = 13;
    var legendSpacing = 18;

    var legend = svg.selectAll('.legend')
        .data(color.domain())
        .enter()
        .append('g')
        .attr('class', 'circle-legend')
        .attr('transform', function(d, i) {
            var height = legendRectSize = legendSpacing;
            var offset = height * color.domain().length / 2;
            var horz = -2 * legendRectSize - 13;
            var vert = i * height - offset;
            return 'translate(' + horz + ',' + vert + ')';
        });

    // Keys
    legend.append('circle')
        .style('fill', color)
        .style('stroke', color)
        .attr('cx', 0)
        .attr('cy', 0)
        .attr('r', '.5rem');

    // Labels
    legend.append('text')
        .attr('x', legendRectSize + legendSpacing)
        .attr('y', legendRectSize - legendSpacing)
        .text(function (d) {
            return d;
        });

    d3.select("button#everyone")
        .on("click", function() {
            change(totals);
        })

    d3.select("button#women")
        .on("click", function() {
            change(femaleData);
        })

    d3.select("button#men")
        .on("click", function() {
            change(maleData);
        })

    function change(data) {
        var pie = d3.pie()
        .value(function (d) {
            return d.value;
        }).sort(null)(data);
    
        var width = 400;
        var height = 400;
        var radius = Math.min(width, height) / 2;
        var donutWidth = 75;
    
        path = d3.select("#donut")
            .selectAll("path")
            .data(pie);
        var arc = d3.arc()
            .innerRadius(radius - donutWidth)
            .outerRadius(radius);
        
        path.transition().duration(500).attr("d", arc);
    
    }


};
