var geocoder;
var map;
var markers = [];

$(document).ready(function() {
    var $select = createMapSelect(locations);
    $select.children().first().attr("selected", "selected");
    $selectedOption = $select.children().first();
    initialize(locations[$selectedOption.data("type")][$select.val()], $selectedOption.data("type"));
    $select.change(function() {
        initializeSelectedMap($(this));
    });
    $('#zoom_out').click(function() {
        initializeSelectedMap($select);
    });
});

function initializeSelectedMap($mapSelect) {
    var selectedLocation = locations[$mapSelect.children(":selected").data("type")][$mapSelect.val()];
    initialize(selectedLocation, $mapSelect.children(":selected").data("type"));
}

function initialize(location, type) {
    clearAddressDisplay();

    if(type == "single") {
        geocoder = new google.maps.Geocoder();
        var latlng = new google.maps.LatLng(location.lat, location.long);
        var mapOptions = {
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);

        deleteMarkers();
        updateAddressDisplay(location);
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
            $option = $('<option />').val(locKey);
            $option.text(locationObj.label);
            $select.append($option);
        }
        $('#loc_select').html($select);
        $select.change(function() {
            locationSelectChange(getCurrentlySelectedLocation($(this).val()));
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
    };

    return locationKeys;
}

function locationSelectChange(location) {
    var mapObj = locations[location.type][location.map];
    var locationObj = mapObj.locations[location.location];
    var position = new google.maps.LatLng(locationObj.lat, locationObj.long);

    if (location.type == 'single') {
        deleteMarkers();
        panAndMarkMap(locationObj);
    } else if (location.type == 'collection') {
        deleteMarkers();
        panAndMarkMap(locationObj);
    }
}

function clearAddressDisplay() {
    $('#addr_container').html('');
}

function updateAddressDisplay(location) {
    $labelP = $('<p />').append('<strong />').text(location.label);
    $addrP = $('<p />').text(location.address);

    $('#addr_container').html($labelP);
    $('#addr_container').append($addrP);
}

function addMarker(location, label, showLabel) {
    var marker = new google.maps.Marker({
        map:map,
        animation: google.maps.Animation.DROP,
        position: location
    });

    var infowindow = new google.maps.InfoWindow({
        content: label,
        position: location
    });

    if(showLabel) {
        infowindow.open(map,marker);
    }

    google.maps.event.addListener(marker, 'click', function() {
        infowindow.open(map,marker);
        map.setZoom(17);
        map.panTo(location);
    });

    markers.push(marker);
}

function makeAddressLabel(label,address) {
    console.log(label + ' ' + address);

    $labelP = $('<span />').html('<strong>' + label + '</strong><br />');
    $addrP = $('<span />').html(address + '<br />');
    $dirA = $('<a />').text('Get Directions');
    $dirA.attr('href','http://maps.google.com/maps?q=' + encodeURIComponent(address));
    $addressLabel = $('<div />').append($labelP).append($addrP).append($dirA);
    return $addressLabel.html();
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
function panSingleMap(single) {
    var LocationBounds = {};
    LocationBounds.latitude = -1;
    LocationBounds.longitude = -1;

    bounds = new google.maps.LatLngBounds();

    var numLocs = 0;
    var locationLatlng;
    var locationObj;
    // loop through the collection and add
    for (var locKey in single.locations) {
        locationObj = single.locations[locKey];
        var lat = locationObj.lat;
        var long = locationObj.long;

        locationLatlng = new google.maps.LatLng(lat,long);
        bounds.extend(locationLatlng);

        map.fitBounds(bounds);
        numLocs++;
    }

    if(numLocs == 1) {
        map.setZoom(17);
        map.panTo(locationLatlng);
        addMarker(locationLatlng, makeAddressLabel(single.label,single.address), true);
        clearSelects();
    } else if (single.hasOwnProperty('lat') && single.hasOwnProperty('long')){
        markerLoc = new google.maps.LatLng(single.lat,single.long);
        bounds.extend(markerLoc);
        map.panToBounds(bounds);
        addMarker(markerLoc, makeAddressLabel(single.label,single.address), true);
        createLocationSelect(single);
    } else {
        map.panToBounds(bounds);
        addMarker(bounds.getCenter(), makeAddressLabel(single.label,single.address), true);
        createLocationSelect(single);
    }
}

// Panning to a single point and marking it
function panAndMarkMap(location) {
    var LocationBounds = {};
    LocationBounds.latitude = -1;
    LocationBounds.longitude = -1;

    var lat = location.lat;
    var long = location.long;

    locationLatlng = new google.maps.LatLng(lat,long);

    map.setZoom(17);
    map.panTo(locationLatlng);

    if(location.address) {
        addMarker(locationLatlng, makeAddressLabel(location.label,location.address), true);
    } else {
        addMarker(locationLatlng, location.label, true);
    }
}

function makeCollectionMap(collection) {
    var LocationBounds = {};
    LocationBounds.latitude = -1;
    LocationBounds.longitude = -1;

    bounds = new google.maps.LatLngBounds();

    // loop through the collection and add
    for (var locKey in collection.locations) {
        var locationObj = collection.locations[locKey];
        var lat = locationObj.lat;
        var long = locationObj.long;

        var locationLatlng = new google.maps.LatLng(lat,long);

        addMarker(locationLatlng, makeAddressLabel(locationObj.label, locationObj.address), false);

        bounds.extend(locationLatlng);

        map.fitBounds(bounds);
    }

    map.panToBounds(bounds);
}
