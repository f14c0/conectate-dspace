'use strict';

/**
 * @ngdoc function
 * @name conectateServices
 * @description
 * # 
 * Services REST for conectateApp
 */

 var conectateServices = angular.module('conectateServices',['ngResource']);

 conectateServices.factory('Items',['$resource',
 	function($resource){
 		return $resource('https://trydspace.longsight.com/rest/items/',{},{
 			get: {method: 'GET', params:{limit:'@limit',offset: '@offset',expand: 'metadata'}, isArray: true}
 		});
 	}]);

 conectateServices.factory('Item',['$resource',
 	function($resource){
 		return $resource('https://trydspace.longsight.com/rest/items/:id/',{},{
 			get: {method: 'GET', params:{id:'@id', expand: 'metadata,parentCollection,bitstreams'}}
 		});
 	}]);

 conectateServices.factory('Meta',['$resource',
 	function($resource){
 		return $resource('https://trydspace.longsight.com/rest/items/55/metadata',{},{
 			get: {method: 'GET', params:{id:'@id'}, isArray: true}
 		});
 	}]);

 conectateServices.factory('Communities', ['$resource',
 	function($resource){
 		return $resource('https://trydspace.longsight.com/rest/communities/',{},{
 			get: {method: 'GET', params:{id:'@id'}, isArray: true}
 		});
 	}]);

 conectateServices.factory('Collections', ['$resource',
 	function($resource){
 		return $resource('https://trydspace.longsight.com/rest/communities/:id/collections',{},{
 			get: {method: 'GET', params:{id:'@id'}, isArray: true}
 		});
 	}]);

 conectateServices.factory('Items_Col', ['$resource',
 	function($resource){
 		return $resource('https://trydspace.longsight.com/rest/collections/:id/items',{},{
 			get: {method: 'GET', params:{id:'@id'}, isArray: true}
 		});
 	}]);

 conectateServices.factory('dataService', function() {
	 var savedData = {};
	 function set(data) {
	   savedData = data;
	 }
	 function get() {
	  return savedData;
	 }

	 return {
	  set: set,
	  get: get
	 };

	});

conectateServices.factory('Search',['$resource',
 	function($resource){
 		return $resource('http://path/to/rest/search.json',{},{
 			query: {method: 'GET', params:{query:'@query'}, isArray: true}
 		});
 	}]);