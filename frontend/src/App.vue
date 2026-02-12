<template>
  <div class="dashboard">
    <header>
      <h1>Server Monitoring Dashboard</h1>
      <div v-if="lastUpdated" class="last-updated">
        Last updated: {{ lastUpdated }}
      </div>
    </header>

    <main>
      <!-- Stat Cards -->
      <div class="stats-grid">
        <StatCard title="CPU Usage" :value="currentStats.cpu_usage" unit="%" icon="cpu" />
        <StatCard title="RAM Usage" :value="currentStats.ram_usage" unit="%" icon="memory" />
        <StatCard title="Disk Usage" :value="currentStats.disk_usage" unit="%" icon="disc" />
        <div class="card status-card">
            <h3>System Status</h3>
            <div :class="['status-indicator', currentStats.status ? currentStats.status.toLowerCase() : '']">
                {{ currentStats.status || 'Loading...' }}
            </div>
        </div>
      </div>

      <!-- Charts -->
      <div class="charts-grid">
        <UsageChart title="CPU History" :labels="historyLabels" :data="cpuHistory" color="#3b82f6" />
        <UsageChart title="RAM History" :labels="historyLabels" :data="ramHistory" color="#8b5cf6" />
      </div>

      <!-- Logs -->
      <LogTable :logs="recentLogs" />
    </main>
  </div>
</template>

<script>
import axios from 'axios';
import StatCard from './components/StatCard.vue';
import UsageChart from './components/UsageChart.vue';
import LogTable from './components/LogTable.vue';

export default {
  name: 'App',
  components: {
    StatCard,
    UsageChart,
    LogTable
  },
  data() {
    return {
      currentStats: {},
      historyLabels: [],
      cpuHistory: [],
      ramHistory: [],
      recentLogs: [],
      lastUpdated: '',
      polling: null
    }
  },
  methods: {
    async fetchData() {
      try {
        // Fetch Current Stats
        const currentRes = await axios.get('http://localhost:8000/stats/current');
        this.currentStats = currentRes.data;
        this.lastUpdated = new Date().toLocaleTimeString();

        // Fetch History
        const historyRes = await axios.get('http://localhost:8000/stats/history');
        const history = historyRes.data;
        
        this.historyLabels = history.map(h => new Date(h.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' }));
        this.cpuHistory = history.map(h => h.cpu_usage);
        this.ramHistory = history.map(h => h.ram_usage);

        // Fetch Logs
        const logsRes = await axios.get('http://localhost:8000/stats/logs');
        this.recentLogs = logsRes.data;

      } catch (error) {
        console.error("Error fetching data:", error);
      }
    }
  },
  mounted() {
    this.fetchData();
    this.polling = setInterval(this.fetchData, 5000); // Poll every 5 seconds
  },
  beforeUnmount() {
    clearInterval(this.polling);
  }
}
</script>

<style>
/* Global Resets */
:root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;
  color: #1f2937;
  background-color: #f3f4f6;
}
body {
  margin: 0;
  min-width: 320px;
  min-height: 100vh;
}

.dashboard {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

h1 {
  font-size: 1.8rem;
  font-weight: 700;
  color: #111827;
  margin: 0;
}

.last-updated {
    font-size: 0.9rem;
    color: #6b7280;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.charts-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-bottom: 2rem;
}

@media (max-width: 768px) {
    .charts-grid {
        grid-template-columns: 1fr;
    }
}

.card {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.status-card h3 {
    margin: 0 0 0.5rem 0;
    font-size: 1rem;
    color: #4b5563;
}

.status-indicator {
    font-size: 1.5rem;
    font-weight: bold;
    color: #6b7280;
}
.status-indicator.healthy { color: #059669; }
.status-indicator.warning { color: #d97706; }
.status-indicator.critical { color: #dc2626; }

</style>
