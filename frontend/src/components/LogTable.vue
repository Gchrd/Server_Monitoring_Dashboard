<template>
  <div class="table-container">
    <h3>Recent Logs</h3>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Time</th>
            <th>CPU</th>
            <th>RAM</th>
            <th>Disk</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="log in logs" :key="log.id">
            <td>{{ formatDate(log.created_at) }}</td>
            <td>{{ log.cpu_usage }}%</td>
            <td>{{ log.ram_usage }}%</td>
            <td>{{ log.disk_usage }}%</td>
            <td>
              <span :class="['status-badge', log.status.toLowerCase()]">
                {{ log.status }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LogTable',
  props: {
    logs: Array
  },
  methods: {
    formatDate(dateString) {
      if (!dateString) return '';
      const date = new Date(dateString);
      return date.toLocaleTimeString();
    }
  }
}
</script>

<style scoped>
.table-container {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  overflow: hidden;
}
h3 {
    margin-top: 0;
    margin-bottom: 1rem;
    color: #4b5563;
}
.table-wrapper {
    overflow-x: auto;
}
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}
th, td {
  padding: 0.75rem 1rem;
  text-align: left;
  border-bottom: 1px solid #e5e7eb;
}
th {
  background-color: #f9fafb;
  font-weight: 600;
  color: #374151;
}
.status-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 600;
}
.healthy {
  background-color: #d1fae5;
  color: #065f46;
}
.warning {
  background-color: #fef3c7;
  color: #92400e;
}
.critical {
  background-color: #fee2e2;
  color: #b91c1c;
}
</style>
