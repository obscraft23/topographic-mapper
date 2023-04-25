let lat0;
let lon0;
let lat1;
let lon1;
// initialize map
var map = L.map('map');
map.setView([36.62335945025434, 137.61721909046176],15); 
L.tileLayer('https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png', {
    attribution: "<a href='https://maps.gsi.go.jp/development/ichiran.html' target='_blank'>国土地理院</a>"
}).addTo(map);

var areaSelect = L.areaSelect({width:200, height:282.842712, keepAspectRatio:true});
areaSelect.on("change", function() {
    var bounds = this.getBounds();
    lat0 = bounds.getSouthWest().lat;
    lon0 = bounds.getSouthWest().lng;
    lat1 = bounds.getNorthEast().lat;
    lon1 = bounds.getNorthEast().lng;
    //$("#result .width").val(bounds.getNorthEast().lat + ", " + bounds.getNorthEast().lng);

});
areaSelect.addTo(map);

var drawnItems = new L.FeatureGroup();
map.addLayer(drawnItems);

var drawControl = new L.Control.Draw({
    edit: {
        featureGroup: drawnItems
    }
});
map.addControl(drawControl);


var toolbar = L.Toolbar();
toolbar.addToolbar(map);