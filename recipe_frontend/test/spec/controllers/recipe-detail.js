'use strict';

describe('Controller: RecipeDetailCtrl', function () {

    // load the controller's module
    beforeEach(module('recipeOrganizerApp'));

    var RecipeDetailCtrl,
        scope;

    // Initialize the controller and a mock scope
    beforeEach(inject(function ($controller, $rootScope) {
        scope = $rootScope.$new();
        RecipeDetailCtrl = $controller('RecipeDetailCtrl', {
            $scope: scope
        });
    }));

    it('should attach a list of awesomeThings to the scope', function () {
        expect(scope.awesomeThings.length).toBe(3);
    })});