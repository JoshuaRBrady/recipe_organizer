'use strict';

/**
 * @ngdoc function
 * @name recipeOrganizerApp.controller:RecipeDetailCtrl
 * @description
 * # RecipeDetailCtrl
 * Controller of the recipeOrganizerApp
 */
angular.module('recipeOrganizerApp')
    .controller('RecipeDetailCtrl', function ($scope, $routeParams, Restangular) {
        $scope.recipeId = $routeParams.recipeId;

        Restangular.one('recipes', $scope.recipeId).customGET().then(function (data) {
            $scope.recipe = data;
        });
    });
