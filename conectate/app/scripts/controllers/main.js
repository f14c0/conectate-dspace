'use strict';

/**
 * @ngdoc function
 * @name conectateApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the conectateApp
 */
angular.module('conectateApp')
  .controller('MainCtrl', ['$scope',
                            '$http',
                            'breadcrumbs',
                            'Items',
                            'dataService',
                            '$window',
                            'Search',
                            'Meta',
                            'Communities',
                            'Collections',
                            'Items_Col',
                            function ($scope, $http,breadcrumbs,Items,dataService,$window,Search,Meta,Communities,Collections, Items_Col) {

    $scope.breadcrumbs = breadcrumbs;
    $scope.currentPage = 1;
  	$scope.pageSize = 6;
    $scope.totalItems = 100;
    $scope.communities=[];
    $scope.collections=[];
    $scope.hideCollections = true;
    $scope.dataTree = [];
    $scope.dataTreeCollection = [];
    var tree;

    //Uso de servicio REST para traer los items
    
    
    $scope.pagination = {
      current: 1
    };

       
    function getResultsPage(limit,offset){
      if (limit === '' && offset === '') {
          $scope.items = Items.get(function(data){
            $scope.getMetadata(data[0].id);  
          });  
      }else{
          $scope.items = Items.get({limit:limit,offset:offset},function(data){
           
            for (var i = 0; i < data.length; i++) {
             
              $scope.items[i].meta =  crearJsonI($scope.items[i].metadata);
              
            }
          });
      }
      
    }

    getResultsPage(20, 0);

    $scope.pageChanged = function(newPage){
      getResultsPage($scope.pageSize,newPage*$scope.pageSize);
    };
    
    $scope.getMetadata = function (id, index){   

        $http.get('https://trydspace.longsight.com/rest/items/'+id+'/metadata').success(function(data){
            //console.log(data);
            $scope.items[index].meta =  crearJsonI(data);
        });

    };

    function crearJsonI(elements){
          var arAux = {};

          for (var i = 0; i < elements.length; i++) {
              arAux[elements[i].key] = elements[i].value;
          }

          return arAux;
      }

            
    $scope.communities = Communities.get(function (data) {
      var dataArr = angular.fromJson(data);
      $scope.dataTree = jsonTojson(dataArr);
      $scope.my_tree = tree = {};  
    });

    

    /**
     ** Funcion para traer las colecciones pertencientes a una comunidad
     **/
    $scope.select_community = function(branch){
      
      $scope.community_name = branch.label;
      $scope.hideCollections = false;

      $scope.collections = Collections.get({id: branch.data[0].id}, function(data){
        var dataArr = angular.fromJson(data);
        $scope.dataTreeCollection = jsonTojson(dataArr);
        $scope.my_tree_col = tree = {};
      });
      
    };

    $scope.select_collection = function(branch){
        $scope.collection_name = branch.label;
        $scope.hideTitleCollection = false;

        $scope.items = Items_Col.get({id: branch.data[0].id},function(data){
           
            for (var i = 0; i < data.length; i++) {
              $scope.getMetadata(data[i].id, i);  
            }
        });
    };

    /**
    **Función que lee el json que llega del API y lo traduce a un objeto que entiende el plugin generador
    **del menú tipo arbol
    **/

    function jsonTojson(elements){
        var treeArr = [];
        console.log(elements.length);
        if(elements.length > 0){
          var i = 0;
        angular.forEach(elements, function(value, key){
          
          treeArr[i] = {label : value.name, children : chlidrenElements(value), data : [{id: value.id}]};
          i++;
        }, treeArr);

      }
        return treeArr;
    }

    function chlidrenElements(element){
      var obj;
      if (angular.isDefined(element.subcommunities) && angular.isArray(element.subcommunities) && element.subcommunities.length > 0) {
                obj = jsonTojson(element.subcommunities);
            }
      return obj;
    }

    $scope.goItem = function(id){
      dataService.set(id);
      $window.location.href = "/#/resources/"+id;
    };

    $scope.search = function(){
      console.log($scope.query);
      $scope.items = Search.query({query:$scope.query});
    };    

  }]).directive('communities', function() {
  return {
    templateUrl: 'views/communities.html'
  };
});
