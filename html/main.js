document.addEventListener("DOMContentLoaded", function (event) {
	var factorf = document.querySelector('.setting-factor');
	var setbtn = document.querySelector('.set-button');
	var stopbtn = document.querySelector('.stop-button');
	var verb = document.querySelector('.verb');	

	var stopped = false;

	var send_xhr = function(addr) {
		var xhr = new XMLHttpRequest();
		xhr.onreadystatechange = function() {
			if (this.readyState == 4 && this.status == 200) {
	   			var data = JSON.parse(xhr.responseText);
				factorf.value = data.factor;
				stopped = !data.running;
				verb.innerHTML = stopped ? 'starten' : 'stoppen';
			}
		};
		xhr.open("GET", addr, true);
		xhr.send();
	};

	send_xhr('/api/status');

	setbtn.addEventListener('click', function() {
		send_xhr('api/setf/'+factorf.value);
	});
	stopbtn.addEventListener('click', function() {
		if (stopped)
			send_xhr('api/start');
		else
			send_xhr('api/stop');
		verb.innerHTML = !stopped ? 'starten' : 'stoppen';
		stopped = !stopped;
	});
});

