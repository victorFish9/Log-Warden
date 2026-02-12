<h1>Log Warden 🛡️</h1>

<p>Log Warden is a lightweight, real-time log monitoring and alerting system designed for Linux environments. It simulates the lifecycle of a production server, parses access logs in real-time to detect error spikes (4xx/5xx HTTP codes), and sends instant notifications via Telegram when thresholds are breached.</p>

<p>This project demonstrates the integration of Python scripting, Bash automation, Systemd services, and Cron jobs to build a robust DevOps tool.</p>

<hr>

<h1>🚀 Key Features</h1>
<ul>
    <li><strong>Log Simulation:</strong> A built-in generator that emulates Nginx traffic with randomized HTTP status codes.</li>
    <li><strong>Real-time Monitoring:</strong> A Python service that "tails" the log file and parses lines on the fly.</li>
    <li><strong>Alerting System:</strong> Trigger-based notifications to Telegram when error rates exceed defined limits (e.g., >5 errors in 60s).</li>
    <li><strong>Daemonization:</strong> Runs as a background system service using systemd.</li>
    <li><strong>Automated Maintenance:</strong> Log rotation and archival using Bash and Cron to prevent disk overflow.</li>
</ul>

<h1>🛠️ Architecture</h1>
<h3>The system consists of three main components:</h3>
<ol>
    <li><strong>The Generator</strong> (<code>log_generator.py</code>): Acts as the web server, writing entry lines to <code>access.log</code>.</li>
    <li><strong>The Warden</strong> (<code>warden.py</code>): Reads <code>access.log</code>, applies logic (Regular Expressions), and manages the alerting window.</li>
    <li><strong>The Cleaner</strong> (<code>rotate_logs.sh</code>): Compresses old logs and cleans up the workspace.</li>
</ol>

<h1>📋 Prerequisites</h1>
<ul>
    <li>Linux/Unix environment (Ubuntu, Debian, MacOS, or WSL).</li>
    <li>Python 3.x.</li>
    <li>Telegram Bot Token (for alerts).</li>
</ul>

<h1>⚙️ Installation & Setup</h1>

<h3>Clone the repository:</h3>
<pre><code>git clone https://github.com/victorFish9/log-warden.git
cd log-warden</code></pre>

<h3>Install dependencies:</h3>
<pre><code>pip install requests</code></pre>

<h3>Configure the Warden:</h3>
<p>Open <code>warden.py</code> and update the configuration section:</p>
<pre><code>TG_TOKEN = "YOUR_BOT_TOKEN"
TG_CHAT_ID = "YOUR_CHAT_ID"
ERROR_THRESHOLD = 5</code></pre>

<h3>Make scripts executable:</h3>
<pre><code>chmod +x rotate_logs.sh</code></pre>

<h1>🖥️ Usage</h1>

<h3>1. Start the Simulation</h3>
<p>Open a terminal and run the generator to start creating fake Nginx logs:</p>
<pre><code>python3 log_generator.py</code></pre>
<p><em>Leave this running in a separate terminal window.</em></p>

<h3>2. Manual Run (Testing)</h3>
<p>Run the Warden manually to see output in the console:</p>
<pre><code>python3 warden.py</code></pre>

<h3>3. Production Run (Systemd)</h3>
<p>To run Log Warden as a background service (Daemon):</p>
<p>Edit <code>logwarden.service</code> and fix the paths to match your directory.</p>
<p>Copy the service file:</p>
<pre><code>sudo cp logwarden.service /etc/systemd/system/</code></pre>

<p>Start and enable the service:</p>
<pre><code>sudo systemctl daemon-reload
sudo systemctl start logwarden
sudo systemctl enable logwarden</code></pre>

<h3>4. Setup Log Rotation (Cron)</h3>
<p>To automatically archive logs every minute (for testing) or daily:</p>
<p>Open crontab:</p>
<pre><code>crontab -e</code></pre>

<p>Add the following line (adjust path):</p>
<pre><code>* * * * * /path/to/log-warden/rotate_logs.sh</code></pre>

<h1>📊 Analytics with Bash (Bonus)</h1>
<p>Since the project uses standard log formats, you can use CLI tools for ad-hoc analysis:</p>

<p><strong>Count 500 Errors:</strong></p>
<pre><code>grep " 500 " access.log | wc -l</code></pre>

<p><strong>Find Top 5 IPs:</strong></p>
<pre><code>awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -5</code></pre>

<h1>🧠 Skills Demonstrated</h1>
<ul>
    <li><strong>Python:</strong> File handling, Regular Expressions (RegEx), API requests, Time management.</li>
    <li><strong>Bash:</strong> File manipulation, Piping, Streams, Text processing (awk, grep).</li>
    <li><strong>Linux Internals:</strong> Understanding systemd unit files, permissions, and cron scheduling.</li>
    <li><strong>DevOps Mindset:</strong> Monitoring, Alerting, and Log Rotation policies.</li>
</ul>
