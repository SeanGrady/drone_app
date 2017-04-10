angular.module('drone_module', [])
    .service('droneService', function($http) {
        var droneService = this;
        droneService.getStatus = function() {
            return $http({
                method: 'GET',
                url: 'http://127.0.0.1:8000/status',
            });
        };
        
        droneService.launchDrone = function() {
            return $http({
                method: 'GET',
                url: 'http://127.0.0.1:8000/launch',
            });
        };

        droneService.landDrone = function() {
            return $http({
                method: 'GET',
                url: 'http://127.0.0.1:8000/land',
            });
        };
    })
    .controller('droneController', function(droneService) {
        var droneController = this;
        //var droneController.curent_status = 'idle';
        droneController.updateStatus = function() {
            droneService.getStatus().then(function(response) {
                droneController.current_status = response.data;
            });
        };
        droneController.launchButton = function() {
            droneService.launchDrone().then(function(response) {
                droneController.current_status = response.data;
            });
        };
        droneController.landButton = function() {
            droneService.landDrone().then(function(response) {
                droneController.current_status = response.data;
            });
        };
    });
