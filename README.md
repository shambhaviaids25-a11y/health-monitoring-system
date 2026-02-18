<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Health Tracker Pro Prototype - Multi-User</title>
    <!-- Load Tailwind CSS for fast, modern styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Chart.js for visualization -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
    <style>
        /* Custom styles for better visual appeal and responsiveness */
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f7f9fb;
        }
        .card {
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s ease;
        }
        .alert-critical {
            animation: pulse-red 1s infinite;
        }
        @keyframes pulse-red {
            0%, 100% { background-color: #fca5a5; box-shadow: 0 0 10px #ef4444; }
            50% { background-color: #ef4444; box-shadow: 0 0 20px #dc2626; }
        }
        /* Custom height for the chart container */
        .chart-container {
            position: relative;
            height: 300px;
            width: 100%;
        }
        /* Style for active tab in navigation */
        .tab-active {
            border-color: #3b82f6; /* blue-500 */
            color: #3b82f6;
            font-weight: 600;
        }
        .profile-select-wrapper {
            transition: all 0.3s;
            border-radius: 0.75rem;
            padding: 1rem;
            background-color: #ffffff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }
    </style>
</head>
<body class="min-h-screen p-4 sm:p-8">

    <div class="max-w-4xl mx-auto">
        <header class="text-center mb-6">
            <h1 class="text-4xl font-extrabold text-blue-700">Health Tracker Pro</h1>
            <p class="text-lg text-gray-500 mt-2">Multi-Profile Health Monitoring Prototype</p>
        </header>
        
        <!-- Profile Selection/Management -->
        <div class="profile-select-wrapper mb-8 border-t-4 border-gray-400">
            <h3 class="text-xl font-bold text-gray-800 mb-3 flex items-center">
                 <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 mr-2 text-gray-600">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a2.25 2.25 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.975M12 9a3.75 3.75 0 1 0 0-7.5 3.75 3.75 0 0 0 0 7.5Z" />
                 </svg>
                Current Profile: <span id="current-profile-name" class="font-extrabold text-blue-600 ml-2">Loading...</span>
            </h3>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <select id="profile-select" class="col-span-2 p-3 border rounded-lg focus:ring-blue-500 focus:border-blue-500"></select>
                <button onclick="addNewProfile()" class="bg-gray-200 text-gray-800 py-2 rounded-lg hover:bg-gray-300 font-medium transition duration-200">
                    + Add New Profile
                </button>
            </div>
        </div>

        <!-- NEW: Navigation Bar -->
        <nav class="flex space-x-4 border-b border-gray-300 mb-6">
            <button id="tab-dashboard" onclick="showSection('dashboard')" 
                    class="py-2 px-4 text-gray-600 border-b-2 border-transparent hover:border-gray-500 transition duration-150">
                Dashboard (Input)
            </button>
            <button id="tab-history" onclick="showSection('history')" 
                    class="py-2 px-4 text-gray-600 border-b-2 border-transparent hover:border-gray-500 transition duration-150">
                History & Trends
            </button>
        </nav>

        <!-- Alerts (Always Visible) -->
        <div id="critical-alert-banner" class="hidden p-4 rounded-xl text-white font-bold text-center alert-critical mb-6">
            🚨 URGENT: CRITICAL HIGH BLOOD PRESSURE! Seek medical advice immediately.
        </div>
        <div id="low-bp-alert-banner" class="hidden p-4 rounded-xl text-amber-900 font-bold text-center bg-yellow-300 mb-6">
            ⚠️ CAUTION: LOW BLOOD PRESSURE DETECTED! Consult your physician if symptomatic.
        </div>

        <!-- Section 1: DASHBOARD (Input and Latest Snapshot) -->
        <div id="dashboard-sections">
            
            <!-- Main Input Form -->
            <div class="bg-white p-6 md:p-8 rounded-xl card mb-10 border-t-4 border-blue-500">
                <h2 class="text-2xl font-bold mb-6 text-gray-800 flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mr-2 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                    </svg>
                    Record Today's Metrics
                </h2>

                <form id="data-form" class="space-y-4">
                    <!-- VITAL INPUTS -->
                    <div class="grid grid-cols-2 gap-4">
                         <div>
                            <label for="weight" class="block text-sm font-medium text-gray-700">Weight (kg)</label>
                            <input type="number" step="0.1" id="weight" name="weight" placeholder="e.g., 75" required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm p-3 focus:ring-blue-500 focus:border-blue-500 border">
                        </div>
                        <div>
                            <label for="height" class="block text-sm font-medium text-gray-700">Height (m)</label>
                            <input type="number" step="0.01" id="height" name="height" placeholder="e.g., 1.75" required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm p-3 focus:ring-blue-500 focus:border-blue-500 border">
                        </div>
                    </div>

                    <!-- METRIC INPUTS -->
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label for="steps" class="block text-sm font-medium text-gray-700">Daily Steps (Fitness)</label>
                            <input type="number" id="steps" name="steps" placeholder="e.g., 7500" required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm p-3 focus:ring-blue-500 focus:border-blue-500 border">
                        </div>
                        <div>
                            <label for="sleep_hrs" class="block text-sm font-medium text-gray-700">Sleep Duration (Hours)</label>
                            <input type="number" step="0.1" id="sleep_hrs" name="sleep_hrs" placeholder="e.g., 7.5" required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm p-3 focus:ring-blue-500 focus:border-blue-500 border">
                        </div>
                    </div>

                    <!-- Blood Pressure Input -->
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label for="bp_systolic" class="block text-sm font-medium text-gray-700">Systolic BP (Top Number)</label>
                            <input type="number" id="bp_systolic" name="bp_systolic" placeholder="e.g., 120" required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm p-3 focus:ring-blue-500 focus:border-blue-500 border">
                        </div>
                        <div>
                            <label for="bp_diastolic" class="block text-sm font-medium text-gray-700">Diastolic BP (Bottom Number)</label>
                            <input type="number" id="bp_diastolic" name="bp_diastolic" placeholder="e.g., 80" required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm p-3 focus:ring-blue-500 focus:border-blue-500 border">
                        </div>
                    </div>

                    <button type="submit" class="w-full bg-blue-600 text-white py-3 mt-4 rounded-xl font-semibold hover:bg-blue-700 transition duration-300 shadow-md hover:shadow-lg">
                        Save Daily Metrics
                    </button>
                </form>
                <div id="message-box" class="mt-4 p-3 rounded-lg text-center font-medium hidden"></div>
            </div>

            <!-- Latest Report Cards (Health Snapshot) -->
            <div id="report-container" class="space-y-6">
                <h2 class="text-3xl font-bold text-gray-800 mb-6 border-b pb-2">Health Snapshot</h2>

                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
                    <!-- BMI Card -->
                    <div class="card p-4 rounded-xl bg-purple-50 border-l-4 border-purple-500 text-center">
                        <div class="text-sm font-semibold text-purple-700 mb-1">BMI</div>
                        <p class="text-3xl font-extrabold text-gray-900" id="bmi-output">--</p>
                        <p class="text-xs text-gray-500" id="bmi-status">Weight/Height Status</p>
                    </div>
                    
                     <!-- Calorie Burn Card -->
                    <div class="card p-4 rounded-xl bg-orange-50 border-l-4 border-orange-500 text-center">
                        <div class="text-sm font-semibold text-orange-700 mb-1">Calorie Burn (Est.)</div>
                        <p class="text-3xl font-extrabold text-gray-900" id="calorie-output">--</p>
                        <p class="text-xs text-gray-500">From Steps Today</p>
                    </div>

                    <!-- Fitness Card -->
                    <div class="card p-4 rounded-xl bg-green-50 border-l-4 border-green-500 text-center">
                        <div class="text-sm font-semibold text-green-700 mb-1">Steps</div>
                        <p class="text-3xl font-extrabold text-gray-900" id="steps-output">--</p>
                        <p class="text-xs text-gray-500" id="fitness-status">Goal Status</p>
                    </div>

                    <!-- Sleep Card -->
                    <div class="card p-4 rounded-xl bg-indigo-50 border-l-4 border-indigo-500 text-center">
                        <div class="text-sm font-semibold text-indigo-700 mb-1">Sleep (hrs)</div>
                        <p class="text-3xl font-extrabold text-gray-900" id="sleep-output">--</p>
                        <p class="text-xs text-gray-500" id="sleep-status">Duration Status</p>
                    </div>
                </div>
                
                <!-- BP Card (Kept separate for prominence) -->
                <div class="bg-white p-6 rounded-xl card border-t-4 border-red-500">
                     <h3 class="text-xl font-bold text-red-700 mb-2 flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
                        </svg>
                        Latest Blood Pressure Reading
                    </h3>
                    <p class="text-6xl font-extrabold text-gray-900" id="bp-output">-- / --</p>
                    <p class="text-lg mt-2" id="bp-status">No data recorded.</p>
                </div>
            </div>
        </div> <!-- End Dashboard Section -->
        
        <!-- Section 2: HISTORY (Visualization and Table) - Hidden by Default -->
        <div id="history-section" class="hidden">
            <!-- Visualization Section -->
            <div id="visualization-section" class="mt-4 bg-white p-6 rounded-xl card-component border-t-4 border-gray-300">
                <h2 class="text-2xl font-bold text-gray-800 mb-4">Daily Steps Trend (Last 7 Days)</h2>
                <div class="chart-container">
                    <canvas id="stepsChart"></canvas>
                </div>
            </div>

            <!-- Historical Data Table Placeholder -->
            <div id="history-container" class="mt-6 bg-white p-6 rounded-xl card-component border-t-4 border-gray-300">
                <h2 class="text-2xl font-bold text-gray-800 mb-4">Historical Data (Last 30 Days)</h2>
                <table class="min-w-full divide-y divide-gray-200">
                    <thead class="bg-gray-50">
                        <tr>
                            <th class="px-3 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Date</th>
                            <th class="px-3 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">BP (S/D)</th>
                            <th class="px-3 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">BMI</th>
                            <th class="px-3 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Steps</th>
                            <th class="px-3 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                        </tr>
                    </thead>
                    <tbody id="data-table-body" class="bg-white divide-y divide-gray-200">
                        <tr><td colspan="5" class="py-4 text-center text-gray-500">No data recorded yet.</td></tr>
                    </tbody>
                </table>
            </div>
        </div> <!-- End History Section -->

        <p class="text-center text-gray-400 mt-10 text-xs">Data is stored locally in your browser (localStorage) for this prototype.</p>
    </div>

    <script>
        // --- GLOBAL STATE ---
        const PROFILE_STORAGE_KEY = 'healthTrackerProfiles';
        let allProfileData = JSON.parse(localStorage.getItem(PROFILE_STORAGE_KEY)) || {};
        let currentProfileId = localStorage.getItem('currentProfileId') || null;
        
        let healthData = []; // Data for the *active* profile only
        let stepsChartInstance = null; // To hold the chart object

        // --- PROFILE MANAGEMENT ---

        function updateProfileList() {
            const select = document.getElementById('profile-select');
            select.innerHTML = '';
            const profileIds = Object.keys(allProfileData);

            if (profileIds.length === 0) {
                // Initial state: No profiles, prompt to add one
                const option = document.createElement('option');
                option.textContent = "--- Add a New Profile ---";
                select.appendChild(option);
                document.getElementById('current-profile-name').textContent = "None Selected";
                return;
            }

            profileIds.forEach(id => {
                const option = document.createElement('option');
                option.value = id;
                option.textContent = id; // Profile ID is the name
                select.appendChild(option);
            });

            // Set the active profile
            if (currentProfileId && profileIds.includes(currentProfileId)) {
                select.value = currentProfileId;
            } else {
                currentProfileId = profileIds[0]; // Default to the first profile
                localStorage.setItem('currentProfileId', currentProfileId);
            }
            
            document.getElementById('current-profile-name').textContent = currentProfileId;
            healthData = allProfileData[currentProfileId] || [];
            renderAllReports();
        }

        function addNewProfile() {
            const newName = prompt("Enter the name for the new profile:");
            if (newName && newName.trim() !== '') {
                const trimmedName = newName.trim();
                if (allProfileData.hasOwnProperty(trimmedName)) {
                    alert(`Profile '${trimmedName}' already exists!`);
                    return;
                }
                
                // Create new profile entry and set as active
                allProfileData[trimmedName] = [];
                currentProfileId = trimmedName;
                
                // Update storage and UI
                localStorage.setItem(PROFILE_STORAGE_KEY, JSON.stringify(allProfileData));
                localStorage.setItem('currentProfileId', currentProfileId);
                
                updateProfileList();
                renderAllReports();
                alert(`Profile '${trimmedName}' created and selected!`);
            }
        }

        function handleProfileChange() {
            const select = document.getElementById('profile-select');
            currentProfileId = select.value;
            localStorage.setItem('currentProfileId', currentProfileId);
            
            document.getElementById('current-profile-name').textContent = currentProfileId;
            
            // Load data for the newly selected profile
            healthData = allProfileData[currentProfileId] || [];
            renderAllReports();
            showSection('dashboard'); // Switch back to dashboard view
        }
        
        // --- 1. CORE LOGIC FUNCTIONS ---
        
        /** Estimates calories burned (approx 0.04 kcal per step). */
        function calculateCaloriesBurned(steps) {
            return steps * 0.04; 
        }

        /** Calculates BMI using kilograms and meters. BMI = weight / (height * height) */
        function calculateBMI(weight, height) {
            if (weight > 0 && height > 0) {
                return weight / (height * height);
            }
            return 0;
        }

        function classifyBMI(bmi) {
            if (bmi < 18.5) return { status: "Underweight", color: "text-amber-600" };
            if (bmi >= 18.5 && bmi <= 24.9) return { status: "Normal Weight", color: "text-green-600" };
            if (bmi >= 25 && bmi <= 29.9) return { status: "Overweight", color: "text-orange-600" };
            return { status: "Obese", color: "text-red-600" };
        }

        /** BP Classification (Original Logic retained) */
        function classifyBloodPressure(s, d) {
            let classification = "Normal";
            let color = "bg-green-500";
            let criticalAlert = false;
            let lowAlert = false;
            
            if (s < 90 && d < 60) {
                 classification = "Hypotension (Low)";
                 color = "bg-yellow-500";
                 lowAlert = true;
            } 
            else if (s >= 140 || d >= 90) {
                classification = "Hypertension Stage 2 (Urgent)";
                color = "bg-red-700";
                criticalAlert = true;
            } 
            else if ((s >= 130 && s <= 139) || (d >= 80 && d <= 89)) {
                classification = "Hypertension Stage 1";
                color = "bg-orange-500";
            }
            else if (s <= 129 && d < 80) {
                classification = "Elevated";
                color = "bg-yellow-500";
            } 
            else if (s < 120 && d < 80) {
                classification = "Normal";
                color = "bg-green-500";
            } 
            else {
                classification = "Atypical Reading";
                color = "bg-gray-500";
            }
            
            return { classification: classification, color: color, criticalAlert: criticalAlert, lowAlert: lowAlert };
        }

        function getSleepAdvice(hrs) {
            if (hrs >= 7 && hrs <= 9) {
                return { status: "Optimal Range", color: "text-indigo-700" };
            } else if (hrs > 9) {
                return { status: "Overslept", color: "text-amber-700" };
            } else {
                return { status: "Needs More Rest", color: "text-red-700" };
            }
        }

        function getFitnessStatus(steps, goal = 7000) {
            if (steps >= goal) {
                return { status: `Goal Achieved!`, color: "text-green-700" };
            } else {
                return { status: `Goal: ${goal.toLocaleString()} Steps`, color: "text-orange-700" };
            }
        }
        
        // --- 2. DATA HANDLERS ---
        
        const form = document.getElementById('data-form');
        const messageBox = document.getElementById('message-box');

        form.addEventListener('submit', function(e) {
            e.preventDefault();

            if (!currentProfileId) {
                messageBox.textContent = `❌ Please add and select a profile first.`;
                messageBox.classList.remove('hidden', 'bg-green-100');
                messageBox.classList.add('bg-red-100', 'text-red-800');
                return;
            }

            const data = {
                date: new Date().toISOString().substring(0, 10), // YYYY-MM-DD for document ID
                timestamp: new Date().getTime(),
                steps: parseInt(document.getElementById('steps').value),
                sleep_hrs: parseFloat(document.getElementById('sleep_hrs').value),
                bp_systolic: parseInt(document.getElementById('bp_systolic').value),
                bp_diastolic: parseInt(document.getElementById('bp_diastolic').value),
                weight: parseFloat(document.getElementById('weight').value),
                height: parseFloat(document.getElementById('height').value)
            };
            
            // Input Validation 
            if (data.bp_systolic < 50 || data.bp_diastolic < 30 || data.weight <= 0 || data.height <= 0) {
                messageBox.textContent = `❌ Invalid input. Please check BP, Weight, and Height values.`;
                messageBox.classList.remove('hidden', 'bg-green-100');
                messageBox.classList.add('bg-red-100', 'text-red-800');
                return;
            }

            // Check if data for today already exists (for upserting)
            const todayIndex = healthData.findIndex(record => record.date === data.date);
            if (todayIndex > -1) {
                healthData[todayIndex] = data;
            } else {
                healthData.push(data);
            }
            
            // Update the global data structure and localStorage
            allProfileData[currentProfileId] = healthData;
            localStorage.setItem(PROFILE_STORAGE_KEY, JSON.stringify(allProfileData));

            messageBox.textContent = `✅ Metrics recorded and saved locally for ${currentProfileId}.`;
            messageBox.classList.remove('hidden', 'bg-red-100', 'bg-red-100');
            messageBox.classList.add('bg-green-100', 'text-green-800');

            // Update the display immediately
            renderAllReports();
            showSection('dashboard'); // Always switch back to dashboard on submit
        });

        // --- 3. RENDERING FUNCTIONS ---
        
        function renderAllReports() {
            // Sort data by date ascending for charts/history display
            healthData.sort((a, b) => new Date(a.date) - new Date(b.date));

            if (healthData.length === 0) {
                // Clear displays if no data for the current profile
                clearReportCards();
                renderHistoricalTable([]);
                renderStepsChart([]);
                return; 
            }

            const latest = healthData[healthData.length - 1];
            
            renderLatestReportCard(latest);
            renderHistoricalTable(healthData);
            renderStepsChart(healthData); 
        }

        function clearReportCards() {
            document.getElementById('bmi-output').textContent = '--';
            document.getElementById('bmi-status').innerHTML = '<span class="text-gray-500">No data.</span>';
            document.getElementById('calorie-output').textContent = '--';
            document.getElementById('steps-output').textContent = '--';
            document.getElementById('fitness-status').innerHTML = '<span class="text-gray-500">No data.</span>';
            document.getElementById('sleep-output').textContent = '--';
            document.getElementById('sleep-status').innerHTML = '<span class="text-gray-500">No data.</span>';
            document.getElementById('bp-output').textContent = '-- / --';
            document.getElementById('bp-status').innerHTML = '<span class="text-gray-500 text-lg">No data recorded.</span>';

            document.getElementById('critical-alert-banner').classList.add('hidden');
            document.getElementById('low-bp-alert-banner').classList.add('hidden');
        }


        function renderLatestReportCard(latest) {
            // 1. BMI Calculation
            const bmi = calculateBMI(latest.weight, latest.height);
            const bmiResult = classifyBMI(bmi);
            document.getElementById('bmi-output').textContent = bmi.toFixed(1);
            document.getElementById('bmi-status').innerHTML = `<span class="${bmiResult.color} font-bold">${bmiResult.status}</span>`;
            
            // 2. Calorie Burn
            const calories = calculateCaloriesBurned(latest.steps);
            document.getElementById('calorie-output').textContent = `${calories.toFixed(0)} kcal`;

            // 3. Fitness
            const fitnessResult = getFitnessStatus(latest.steps);
            document.getElementById('steps-output').textContent = `${latest.steps.toLocaleString()}`;
            document.getElementById('fitness-status').innerHTML = `<span class="${fitnessResult.color} text-xs font-bold">${fitnessResult.status}</span>`;

            // 4. Sleep
            const sleepResult = getSleepAdvice(latest.sleep_hrs);
            document.getElementById('sleep-output').textContent = `${latest.sleep_hrs.toFixed(1)} hrs`;
            document.getElementById('sleep-status').innerHTML = `<span class="${sleepResult.color} text-xs font-bold">${sleepResult.status}</span>`;

            // 5. Blood Pressure
            const bpResult = classifyBloodPressure(latest.bp_systolic, latest.bp_diastolic);
            document.getElementById('bp-output').textContent = `${latest.bp_systolic} / ${latest.bp_diastolic}`;
            document.getElementById('bp-status').innerHTML = `<span class="text-lg font-bold" style="color: ${bpResult.color.replace('bg', 'text')};">${bpResult.classification}</span>`;
            
            // Handle Alert Banners
            const criticalBanner = document.getElementById('critical-alert-banner');
            const lowBanner = document.getElementById('low-bp-alert-banner');
            
            criticalBanner.classList.add('hidden');
            lowBanner.classList.add('hidden');

            if (bpResult.criticalAlert) {
                criticalBanner.classList.remove('hidden');
            } else if (bpResult.lowAlert) {
                lowBanner.classList.remove('hidden');
            }
        }

        function renderHistoricalTable(historyData) {
            const tbody = document.getElementById('data-table-body');
            tbody.innerHTML = ''; // Clear existing rows

            // --- CORRECTED FIX: Show last 30 days, sorted descending (newest first) ---
            const displayData = historyData.slice(-30).reverse();

            if (displayData.length === 0) {
                tbody.innerHTML = '<tr><td colspan="5" class="py-4 text-center text-gray-500">No data recorded for this profile.</td></tr>';
                return;
            }

            displayData.forEach(record => {
                const bpResult = classifyBloodPressure(record.bp_systolic, record.bp_diastolic);
                const bmi = calculateBMI(record.weight, record.height);

                const row = document.createElement('tr');
                row.className = 'hover:bg-gray-50';
                row.innerHTML = `
                    <td class="px-3 py-2 whitespace-nowrap text-sm font-medium text-gray-900">${record.date}</td>
                    <td class="px-3 py-2 whitespace-nowrap text-sm text-gray-700">${record.bp_systolic}/${record.bp_diastolic}</td>
                    <td class="px-3 py-2 whitespace-nowrap text-sm text-gray-700">${bmi.toFixed(1)}</td>
                    <td class="px-3 py-2 whitespace-nowrap text-sm text-gray-700">${record.steps.toLocaleString()}</td>
                    <td class="px-3 py-2 whitespace-nowrap text-xs">
                        <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full text-white" 
                              style="background-color: ${bpResult.color.replace('bg-', '')}">
                            ${bpResult.classification}
                        </span>
                    </td>
                `;
                tbody.appendChild(row);
            });
        }
        
        /** CHART FUNCTIONALITY **/
        function renderStepsChart(data) {
            if (stepsChartInstance) {
                stepsChartInstance.destroy(); // Destroy previous instance if exists
            }

            // Get last 7 days of data for the chart visualization 
            const chartData = data.slice(-7); 
            const labels = chartData.map(record => record.date.substring(5)); // Show MM-DD
            const steps = chartData.map(record => record.steps);

            const ctx = document.getElementById('stepsChart').getContext('2d');
            
            stepsChartInstance = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Daily Steps',
                        data: steps,
                        borderColor: '#3b82f6', // blue-500
                        backgroundColor: 'rgba(59, 130, 246, 0.2)',
                        tension: 0.3,
                        borderWidth: 2,
                        fill: true,
                        pointRadius: 5
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Steps'
                            }
                        }
                    },
                    plugins: {
                        legend: {
                            display: false
                        }
                    }
                }
            });
             
        }

        /** NAVIGATION LOGIC **/
        window.showSection = function(sectionId) {
            const dashboardSection = document.getElementById('dashboard-sections');
            const historySection = document.getElementById('history-section');
            const dashboardTab = document.getElementById('tab-dashboard');
            const historyTab = document.getElementById('tab-history');

            // Reset tab styles
            dashboardTab.classList.remove('tab-active');
            historyTab.classList.remove('tab-active');

            if (sectionId === 'dashboard') {
                dashboardSection.classList.remove('hidden');
                historySection.classList.add('hidden');
                dashboardTab.classList.add('tab-active');
            } else if (sectionId === 'history') {
                dashboardSection.classList.add('hidden');
                historySection.classList.remove('hidden');
                historyTab.classList.add('tab-active');
                
                // Important: Re-render chart whenever the history tab is shown
                renderStepsChart(healthData); 
            }
        }

        // --- INITIALIZATION ---
        
        document.getElementById('profile-select').addEventListener('change', handleProfileChange);
        window.addNewProfile = addNewProfile; // Make function globally accessible

        document.addEventListener('DOMContentLoaded', function() {
            // Check if this is the very first run (no profiles exist)
            if (Object.keys(allProfileData).length === 0) {
                // Prompt user to create the first profile
                const initialName = prompt("Welcome! Please enter a name for the first user profile:");
                if (initialName && initialName.trim() !== '') {
                    allProfileData[initialName.trim()] = [];
                    currentProfileId = initialName.trim();
                    localStorage.setItem(PROFILE_STORAGE_KEY, JSON.stringify(allProfileData));
                    localStorage.setItem('currentProfileId', currentProfileId);
                }
            }

            updateProfileList();
            renderAllReports();
            showSection('dashboard'); // Show Dashboard by default

            // If no profile is active after setup, disable the form
            if (!currentProfileId) {
                document.getElementById('data-form').classList.add('opacity-50', 'pointer-events-none');
                document.getElementById('message-box').textContent = "Please use 'Add New Profile' to start tracking.";
                document.getElementById('message-box').classList.remove('hidden');
            }
        });
    </script>
</body>
</html>
