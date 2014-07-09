'use strict';

/**
 * @ngdoc overview
 * @name recipeOrganizerApp
 * @description
 * # recipeOrganizerApp
 *
 * Main module of the application.
 */

angular
    .module('recipeOrganizerApp', [
        'ngAnimate',
        'ngCookies',
        'ngResource',
        'ngRoute',
        'ngSanitize',
        'ngTouch',
        'restangular'
    ])
    .config(function ($routeProvider, RestangularProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'views/all_recipes.html',
                controller: 'AllRecipesCtrl'
            })
            .when('/my_recipes', {
                templateUrl: 'views/my_recipes.html',
                controller: 'MyRecipesCtrl'
            })
            .when('/contact', {
                templateUrl: 'views/contact.html',
                controller: 'ContactCtrl'
            })
            .when('/recipes/:recipeId', {
                templateUrl: 'views/recipe_detail.html',
                controller: 'RecipeDetailCtrl'
            })
            .when('/add_recipe', {
                templateUrl: 'views/add_recipe.html',
                controller: 'AddRecipeCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });
        RestangularProvider.setBaseUrl('http://localhost:8001')

    });
