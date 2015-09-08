'use strict';

/**
 * @ngdoc function
 * @name conectateApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the conectateApp
 */
angular.module('conectateApp')
  .controller('MainCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  }).directive('communities', function() {
  return {
    templateUrl: 'views/communities.html'
  };
});
