var taskManager = angular.module('taskManager');
taskManager.controller('taskController', function ($scope, $http) {

	var loadData = function () {
		$http.get('/task/list').done(function success(response) {
		$scope.tasks = response.data;
    })} 
	
	loadData()

	$scope.obj = {editing: false}

    $scope.add = function (text) {
        if(text != "")
        {
        	$http.post('/task/add', {'text': text}).done(loadData)
        }
    };
    $scope.delete = function (task) {
    	var url = '/task/' + task.id + '/delete'
    	$http.delete(url).done(loadData())
    };
    $scope.edit = function (task, edited_text) {
    	var url = '/task/' + task.id + '/edit'
    	$http.patch(url, {'text': edited_text}).done(function () {
    		$scope.editing = false
    		return loadData()
    	})
    }
})