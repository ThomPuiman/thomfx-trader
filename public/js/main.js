$(function(){
    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(getChartData);

    function getChartData(){
        $.getJSON( "http://localhost:3333/graph/candle", buildChart);
    }

    function buildChart(data){
        var data = google.visualization.arrayToDataTable(data.map(function(x){
            x[0] = new Date(Date.parse(x[0]));
            return x;  
        }), true);

        var formatter = new google.visualization.NumberFormat(
            {fractionDigits: 6}
        );
        formatter.format(data, 1);
        formatter.format(data, 2);
        formatter.format(data, 3);
        formatter.format(data, 4);

        var options = {
            legend:'none'
            };

        var chart = new google.visualization.CandlestickChart(document.getElementById('chart_div'));

        chart.draw(data, options);
    }
});