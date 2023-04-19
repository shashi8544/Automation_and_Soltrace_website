var P, V, P2, V2, P3, V3, P4, V4;
var data = [];
var DATA = [];

function runProgram() {
	var values=[Number(document.getElementById('input').Th.value),
	Number(document.getElementById('input').Tc.value),
	Number(document.getElementById('input').CR.value),
	Number(document.getElementById('input').R.value),
	Number(document.getElementById('input').P1.value),
	Number(document.getElementById('input').V1.value),
	Number(document.getElementById('input').Qin.value)];
	var vLen = values.length;

    // Input Status Checks
  var status = "Calculation Status: Inputs OK";
	
	// Ensure Positive Numbers
	for (i = 0; i < (vLen-1); i++) {
		if (values[i] < 0) {
			status = "Calculation Status: Please input positive numbers only";
		}	
	}
	
	// Ensure Th is higher than Tc
	if (values[1] >= values [0]) {
		status = "Calculation Status: Please enusre hot end temp is higher than cold end temp";
	}
	
	// Ensure compression ratio is higher than 1
	if (values[2] <= 1) {
		status = "Calculation Status: Please enter a compression ratio higher than 1";
	}
	
	// Ensure a state 1 pressure is entered
		if (values[4] <= 0) {
		status = "Calculation Status: Please enter a state 1 pressure above 0";
	}
	
	// Ensure a volume 1 is entered
		if (values[5] <= 0) {
		status = "Calculation Status: Please enter a state 1 volume above 0";
	}
	
	document.getElementById('inputStatus').innerHTML = status;
	
	// If all inputs OK then run program
	if (status == "Calculation Status: Inputs OK") {
		idealSimulation(values[0],values[1],values[2],values[3],values[4] * 1e3,values[5] * 1e-6,values[6]);
		plotData();
		efficiencyPlot();
	}
}	


function idealSimulation(Th,Tc,CR,R,P1,V1,Qin) {
	P = [];
	V = [];
	var nT = 20; //Number of temperature steps to take between state 2-3 and state 4-1
	var nV = 20; //Number of volume steps to take between state 1-2 and state 3-4
	var v1 = 1 / (P1 / (R * Tc)); //Specific volume of gas at beginning of isothermal compression, state 1 (kg/m^3)
	var dT = (Th - Tc) / nT; //Calculate temperature step size based on the number of steps specified by nT (K)
	var w = R * Tc * Math.log((1 / CR)) + R * Th * Math.log(CR); //Specific mechanical work out per cycle (J/kg)
	var mfluid = V1 / v1; //Mass of working fluid in engine (kg)
	var Vswept = V1 / (CR / (CR - 1)); //Swept volume (m^3)
	var W = w * mfluid; //Mechanical work output per cycle (J)
	var n = 1 - (Tc / Th); //Efficiency with perfect regnerator
	var Freq = (Qin * n) / W; //Predicted engine operating frequency (Hz)
	var RPM = Freq * 60; //Predicted engine operating speed (rev/min)
	var Pout = W * Freq; //Power out of engine (W)
	V2 = V1 - Vswept; //Volume at state 2 (m^3)
	var dV = (V1 - V2) / nV; //Calculate the volume step size based on the number of steps specified by nV (m^3)
	var v = [];
	var T = [];
	var Ptotal = 0;
	for (s = 0; s < 4; s++) { //Calculate P, V, and T for all processes
		if (s == 0) { //Process 1-2
			for (i = 0; i < (nV); i++) {
				V.push(V1 - (i+1) * dV); //Engine volume at given step (m^3)
				v.push(V[i] / mfluid);  //Specific volume at given step (m^3/kg)
				P.push((P1 * V1) / V[i]);  //Pressure at given step, by applying a polytropic process (Pa)
				T.push(Tc); //Temperature at given step (K)
				Ptotal += P[i];
			}
		}
		if (s == 1) { //Process 2-3
			for (i = nV; i < (nT + nV); i++) {
				V.push(V[i-1]); //Engine volume at given step (m^3)
				v.push(V[i] / mfluid); //Specific volume at given step (m^3/kg)
				T.push(T[i-1] + dT); //Temperature at given step (K)
				P.push((R * T[i]) / v[i]); //Pressure at a given step (Pa)
				Ptotal += P[i];
			}	

		}
		if (s == 2) { //Process 3-4
			for (i = (nT + nV); i < (nT + 2 * nV); i++) {
				V.push(V[i-1] + dV); //Engine volume at given step (m^3)
				v.push(V[i] / mfluid); //Specific volume at given step (m^3/kg)
				P.push((P[nT + nV - 1] * V2) / V[i]); //Pressure at given step, by applying a polytropic process (Pa)
				T.push(Th); //Temperature at given step (K)
				Ptotal += P[i];
			}	
		}
		if (s == 3) { //Process 4-1
			for (i = (nT + 2 * nV); i < (2 * nT + 2 * nV); i++) {
				V.push(V[i-1]); //Engine volume at given step (m^3)
				v.push(V[i] / mfluid); //Specific volume at given step (m^3/kg)
				T.push(T[i-1] - dT); //Temperature at given step (K)
				P.push((R * T[i]) / v[i]); //Pressure at a given step (Pa)
				Ptotal += P[i];
			}
		}
	}
	
	var Pavg = Ptotal / P.length;
	var T1 = T[2 * nT + 2 * nV - 1];
	P2 = P[nV - 1];
	var T2 = T[nV - 1];
	V3 = V[nT + nV - 1];
	P3 = P[nT + nV - 1];
	var T3 = T[nT + nV - 1];
	V4 = V[nT + 2 * nV - 1];
	P4 = P[nT + 2 * nV - 1];
	var T4 = T[nT + 2 * nV - 1];
	document.getElementById('predRPM').innerHTML = RPM.toPrecision(4);
	document.getElementById('predPout').innerHTML = Pout.toPrecision(4);
	document.getElementById('predn').innerHTML = n.toPrecision(4);
	document.getElementById('predPavg').innerHTML = (Pavg * 1e-3).toPrecision(4); //Pa to kPa
	document.getElementById('predVswept').innerHTML = (Vswept * 1e6).toPrecision(4); //m^3 to cc
	document.getElementById('predmfluid').innerHTML = (mfluid * 1e6).toPrecision(4); //kg to mg
	document.getElementById('predW').innerHTML = W.toPrecision(4);
	document.getElementById('predw').innerHTML = (w * 1e-6).toPrecision(4); //J/kg to J/mg
	document.getElementById('predV1').innerHTML = (V1 * 1e6).toPrecision(4); //m^3 to cc
	document.getElementById('predP1').innerHTML = (P1 * 1e-3).toPrecision(4); //Pa to kPa
	document.getElementById('predT1').innerHTML = T1.toPrecision(4);
	document.getElementById('predV2').innerHTML = (V2 * 1e6).toPrecision(4); //m^3 to cc
	document.getElementById('predP2').innerHTML = (P2 * 1e-3).toPrecision(4); //Pa to kPa
	document.getElementById('predT2').innerHTML = T2.toPrecision(4);
	document.getElementById('predV3').innerHTML = (V3 * 1e6).toPrecision(4); //m^3 to cc
	document.getElementById('predP3').innerHTML = (P3 * 1e-3).toPrecision(4); //Pa to kPa
	document.getElementById('predT3').innerHTML = T3.toPrecision(4);
	document.getElementById('predV4').innerHTML = (V4 * 1e6).toPrecision(4); //m^3 to cc
	document.getElementById('predP4').innerHTML = (P4 * 1e-3).toPrecision(4); //Pa to kPa
	document.getElementById('predT4').innerHTML = T4.toPrecision(4);
}

function plotData() {
		
	var PkPa=[];
	var Vcc=[];
	
	var layout = {
		title:'P-V Plot for Your Ideal Stirling Cycle',
		xaxis: {
			title: 'Volume (cc)'
		},
		yaxis: {
			title: 'Pressure (kPa)'
		}
	};
	
	for (i = 0; i<P.length; i++) {
		Vcc[i]=V[i] * 1e6;
		PkPa[i]=P[i] * 1e-3;
	}
	Vcc.push(Vcc[0]); //Add the first point to the end of the volume array to close the loop
	PkPa.push(PkPa[0]); //Add the first point to the end of the pressure array to close the loop
	
	var trace1 = {
		x: Vcc,
		y: PkPa,
		mode: 'lines',
		name: 'path',
		type: 'scatter'
		}
		
	var trace2 = {
		x: [Vcc[(Vcc.length-2)]],
		y: [PkPa[(PkPa.length-2)]],
		mode: 'markers',
		type: 'scatter',
		name: 'state 1',
		marker: {size: 18}
		}
	
	var trace3 = {
		x: [V2 * 1e6],
		y: [P2 * 1e-3],
		mode: 'markers',
		type: 'scatter',
		name: 'state 2',
		marker: {size: 18}
		}
		
	var trace4 = {
		x: [V3 * 1e6],
		y: [P3 * 1e-3],
		mode: 'markers',
		type: 'scatter',
		name: 'state 3',
		marker: {size: 18}
		}
		
	var trace5 = {
		x: [V4 * 1e6],
		y: [P4 * 1e-3],
		mode: 'markers',
		type: 'scatter',
		name: 'state 4',
		marker: {size: 18}
		}
	
	data.push(trace1);
	data.push(trace2);
	data.push(trace3);
	data.push(trace4);
	data.push(trace5);
		
	Plotly.newPlot(document.getElementById('pvPlot'), data, layout);
}

function blankPlot() {
	var layoutPVplot = {
		title:'P-V Plot for Your Ideal Stirling Cycle',
		xaxis: {
			title: 'Volume (cc)'
		},
		yaxis: {
			title: 'Pressure (kPa)'
		}
	};
	
	var Tc = Math.round(Number(document.getElementById('input').Tc.value));
	var layoutEplot = {
		title:'Carnot and Stirling Efficiency vs. Th',
		xaxis: {
			title: 'Th (K)'
		},
		yaxis: {
			title: 'Efficiency (0-1)'
		}
	};
	
	var TRACE1 = {
		x: [],
		y: [],
		mode: 'marker',
		name: 'Tc = ' + Tc + ' K',
		type: 'scatter'
		}
	
	DATA = [];
	data = [];
	var blankData = [TRACE1];
		
	Plotly.newPlot(document.getElementById('pvPlot'), blankData, layoutPVplot);
	Plotly.newPlot(document.getElementById('ePlot'), blankData, layoutEplot);
}

function clearPlot() {
	Plotly.purge('pvPlot');
	Plotly.purge('ePlot');
	blankPlot();
}

function efficiencyPlot() {
	var Tc = Math.round(Number(document.getElementById('input').Tc.value));
	var Th = [];
	var n = [];
	for (i = Tc; i < (Tc + 1000); i++) {
		Th[i - Tc] = i;
		n[i - Tc] = 1 - (Tc / Th[i - Tc]);
	}
	
	var layout = {
		title: 'Carnot and Stirling Efficiency vs. Th',
		xaxis: {
			title: 'Th (K)'
		},
		yaxis: {
			title: 'Efficiency (0-1)'
		},
		showlegend: true
	};
	
	var TRACE1 = {
		x: Th,
		y: n,
		mode: 'marker',
		name: 'Tc = ' + Tc + ' K',
		type: 'scatter'
		}
		
	DATA.push(TRACE1);
	
	Plotly.newPlot(document.getElementById('ePlot'), DATA, layout);
}