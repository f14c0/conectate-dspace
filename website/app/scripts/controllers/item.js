'use strict';

/**
 * @ngdoc function
 * @name conectateApp.controller:ItemCtrl
 * @description
 * # ItemCtrl
 * Controller of the conectateApp
 */
 angular.module('conectateApp')
 	.controller('ItemCtrl', ['$scope',
 							  '$http',
 							  'breadcrumbs',
 							  '$modal',
 							  'dataService',
 							  'Item',
 							  '$route', function ($scope, $http,breadcrumbs,$modal,dataService,Item,$route) {
 		
 		$scope.breadcrumbs = breadcrumbs;
 		
 		$scope.id = $route.current.params.itemId;
 		$scope.item = Item.get({id:$scope.id},function(data){
 			$scope.item.meta = crearJsonI(data.metadata);
 		});


    	function crearJsonI(elements){
	        var arAux = {};
	        for (var i = 0; i < elements.length; i++) {
	            arAux[elements[i].key] = elements[i].value;
	        }

	        return arAux;
    	}
		
	    $scope.open = function (size) {

		    $modal.open({
		      animation: $scope.animationsEnabled,
		      templateUrl: 'myModalContent.html',
		      controller: 'ModalInstanceCtrl',
		      size: size,
		      resolve: {
		        items: function () {
		          return $scope.item;
		        }
		      }
	    	});
	
		};

		$scope.downloadBit = function(){
			console.log($scope.item.bitstreams.length);
			for (var i = 0; i < $scope.item.bitstreams.length; i++) {
				getBit($scope.item.bitstreams[i].retrieveLink, $scope.item.bitstreams[i].mimeType,$scope.item.bitstreams[i].name);
			}
		};

		function getBit(path, bit, fileName){
			$http.get('https://trydspace.longsight.com/rest'+path,{ responseType: 'arraybuffer' }).success(function(data){
		            
		            var file = new Blob([data], {type: bit});
		            saveAs(file, fileName);
		            
	        });
		}


 	}]);

angular.module('conectateApp').controller('ModalInstanceCtrl', function ($scope, $modalInstance, items) {

	$scope.item = items;

	$scope.ok = function () {
	    $modalInstance.close();
	};

	$scope.cancel = function () {
	    $modalInstance.dismiss('cancel');
	};
});