var geocoder;
var map;
var addressArray = new Array();
var resultsArray = new Array();

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
            zoom: location.zoom,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        }
        map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);

        createBuildingSelect(location);
    } else if (type == "collection") {
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

function createBuildingSelect(campus) {
    clearSelects();
    if(campus.hasOwnProperty('buildings')) {
        var $select = $('<select />');
        for(var building in campus.buildings) {
            var buildingObj = campus.buildings[building];
            var $option = $('<option />').val(building);
            $option.text(buildingObj.label);
            $select.append($option);
        }
        $('#bldg_select').html($select);
    }
}

function createLocationSelect(collection) {
    clearSelects();
    if(collection.hasOwnProperty('locations')) {
        var $select = $('<select />');
        for(var locKey in collection.locations) {
            var locationObj = collection.locations[locKey];
            var $option = $('<option />').val(locKey);
            $option.text(locationObj.label);
            $select.append($option);
        }
        $('#loc_select').html($select);
    }
}

function clearSelects() {
    $('#bldg_select').html('');
    $('#loc_select').html('');
}

// function makeLocationMap(locations) {
//     for(campus in locations.single) {
//         var campus = locations.single[campus];
//         console.log(campus.lat);
//         console.log(campus.long);
//         console.log(campus.label);
//         console.log(campus.address);
//         for(building in campus.buildings) {
//             var building = campus.buildings[building];
//             console.log(building.label);
//         }
//     }
// }

// function makeCollectionMap(geoArray) {
//     var LocationBounds = new Object();
//     LocationBounds.latitude = -1;
//     LocationBounds.longitude = -1;
//
//     bounds = new google.maps.LatLngBounds();
//
//     for (var x = 0; x < geoArray.length; x++)
//     {
//
//         var marker = new google.maps.Marker({
//             map: map,
//             position: results[0].geometry.location//,
//             //icon: icon
//         });
//         // adding an event listener
//         // this has to be done for each marker independently
//         google.maps.event.addListener(marker, 'click', function() {
//
//         });
//
//         bounds.extend(results[0].geometry.location);
//         if (x === geoArray.length - 1) {
//             map.fitBounds(bounds);
//             // TODO check if this is a single job map
//             map.setZoom(16);
//         }
//
//     }
//     map.panToBounds(bounds);
// }

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

        var marker = new google.maps.Marker({
            position: locationLatlng,
            map: map,
            title: locationObj.label
        });

        // adding an event listener
        // this has to be done for each marker independently
        google.maps.event.addListener(marker, 'click', function() {

        });

        bounds.extend(locationLatlng);

        map.fitBounds(bounds);
        // TODO check if this is a single job map
        // map.setZoom(16);
    }

    map.panToBounds(bounds);
}
