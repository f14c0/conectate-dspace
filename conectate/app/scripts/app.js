'use strict';

/**
 * @ngdoc overview
 * @name conectateApp
 * @description
 * # conectateApp
 *
 * Main module of the application.
 */
angular
  .module('conectateApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'angularUtils.directives.dirPagination',
    'angularBootstrapNavTree',
    'ng-breadcrumbs',
    'ui.bootstrap',
    'conectateServices'
  ])
  .config(function ($routeProvider,paginationTemplateProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main',
        label: 'Incio'
      })
      .when('/resources/:itemId', {
        templateUrl: 'views/itemView.html',
        controller: 'ItemCtrl',
        controllerAs: 'item',
        label: 'recurso'
      })
      .otherwise({
        redirectTo: '/'
      });
      paginationTemplateProvider.setPath('views/dirPagination.tpl.html');
  });
