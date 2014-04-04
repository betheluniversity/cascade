var geocoder;
var map;
var markers = [];

$(document).ready(function() {
    var $select = createMapSelect(locations);
    $select.children().first().attr("selected", "selected");
    $selectedOption = $select.children().first();
    initialize(locations[$selectedOption.data("type")][$select.val()], $selectedOption.data("type"));
    $select.change(function() {
        var selectedLocation = locations[$(this).children(":selected").data("type")][$(this).val()];
        initialize(selectedLocation, $(this).children(":selected").data("type"));
    });
});

function initialize(location, type) {

    if(type == "single") {
        geocoder = new google.maps.Geocoder();
        var latlng = new google.maps.LatLng(location.lat, location.long);
        var mapOptions = {
            //zoom: location.zoom,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        }
        map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);

        deleteMarkers();
        panSingleMap(location);
    } else if (type == "collection") {
        deleteMarkers();
        makeCollectionMap(location);
        createLocationSelect(location);
    }
}

function createMapSelect(locations) {
    var $select = $('<select />');
    for(var group in locations) {
        for(var collection in locations[group]) {
            var collectionObj = locations[group][collection];
            var $option = $('<option />').val(collection);
            $option.text(collectionObj.label);
            $option.data("type", group);
            $select.append($option);
        }
    }
    $('#map_select').append($select);

    return $select;
}

function createLocationSelect(map) {
    clearSelects();
    if(map.hasOwnProperty('locations')) {
        var $select = $('<select />');
        var $option = $('<option />').text('Select a Location');
        $select.append($option);
        for(var locKey in map.locations) {
            var locationObj = map.locations[locKey];
            var $option = $('<option />').val(locKey);
            $option.text(locationObj.label);
            $select.append($option);
        }
        $('#loc_select').html($select);
        $select.change(function() {
            locationSelectChange(getCurrentlySelectedLocation($(this).val()))
        });
    }
}

function getCurrentlySelectedLocation(location) {
    var map = $('#map_select select').val();
    var type = $('#map_select :selected').data('type');

    var locationKeys = {
        "type": type,
        "map": map,
        "location": location
    }

    return locationKeys;
}

function locationSelectChange(location) {
    var mapObj = locations[location.type][location.map];
    var locationObj = mapObj.locations[location.location];
    var position = new google.maps.LatLng(locationObj.lat, locationObj.long);

    if (location.type == 'single') {
        deleteMarkers();
        panSingleMap(mapObj);
        addMarker(position, locationObj.label);
    } else if (location.type == 'collection') {
        if(map.zoom < 15) {
            map.setZoom(17);
        }

        map.panTo(position);
    }
}

function addMarker(location, label) {
    var marker = new google.maps.Marker({
        map:map,
        animation: google.maps.Animation.DROP,
        position: location,
        title: label
    });

    var infowindow = new google.maps.InfoWindow({
        content: marker.title,
        position: location
    });

    google.maps.event.addListener(marker, 'click', function() {
        infowindow.open(map,marker);
        map.setZoom(18);
        map.panTo(location);

    });

    markers.push(marker);
}

// Removes the markers from the map, but keeps them in the array.
function clearMarkers() {
    setAllMap(null);
}

// Shows any markers currently in the array.
function showMarkers() {
  setAllMap(map);
}

// Deletes all markers in the array by removing references to them.
function deleteMarkers() {
  clearMarkers();
  markers = [];
}

function setAllMap(map) {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(map);
  }
}

function clearSelects() {
    $('#loc_select').html('');
}

// Fitting a single map to the locations defined in it
function panSingleMap(single)
{
    var LocationBounds = new Object();
    LocationBounds.latitude = -1;
    LocationBounds.longitude = -1;

    bounds = new google.maps.LatLngBounds();

    var numLocs = 0;
    var locationLatlng;
    var locationObj;
    // loop through the collection and add
    for (locKey in single.locations) {
        locationObj = single.locations[locKey];
        var lat = locationObj.lat;
        var long = locationObj.long;

        locationLatlng = new google.maps.LatLng(lat,long);
        bounds.extend(locationLatlng);

        map.fitBounds(bounds);
        numLocs++;
    }

    if(numLocs < 2) {
        map.setZoom(19);
        map.panTo(locationLatlng);
        addMarker(locationLatlng, locationObj.label);
        clearSelects();
    } else {
        map.panToBounds(bounds);
        createLocationSelect(single);
    }

}

function makeCollectionMap(collection)
{
    var LocationBounds = new Object();
    LocationBounds.latitude = -1;
    LocationBounds.longitude = -1;

    bounds = new google.maps.LatLngBounds();

    // loop through the collection and add
    for (locKey in collection.locations) {
        var locationObj = collection.locations[locKey];
        var lat = locationObj.lat;
        var long = locationObj.long;

        var locationLatlng = new google.maps.LatLng(lat,long);

        addMarker(locationLatlng, locationObj.label);

        bounds.extend(locationLatlng);

        map.fitBounds(bounds);
        // TODO check if this is a single job map
        // map.setZoom(16);
    }

    map.panToBounds(bounds);
}
