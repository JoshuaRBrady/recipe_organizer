'use strict';

/**
 * @ngdoc function
 * @name recipeOrganizerApp.controller:AllRecipesCtrl
 * @description
 * # AllRecipesCtrl
 * Controller of the recipeOrganizerApp
 */
angular.module('recipeOrganizerApp')
    .controller('AllRecipesCtrl', function ($scope, Restangular) {
        Restangular.all('recipes').getList().then(function (data) {
            $scope.recipes = data;
        });
    });
