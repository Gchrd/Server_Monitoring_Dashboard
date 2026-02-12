<template>
  <div class="stat-card">
    <div class="stat-header">
        <h3>{{ title }}</h3>
        <!-- Simple icon placeholder -->
        <span class="icon">{{ icon === 'cpu' ? '⚡' : icon === 'memory' ? '🧠' : '💾' }}</span>
    </div>
    <div class="stat-value">
        {{ value !== undefined ? value : '--' }}
        <span class="unit">{{ unit }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StatCard',
  props: {
    title: String,
    value: Number,
    unit: String,
    icon: String
  }
}
</script>

<style scoped>
.stat-card {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  display: flex;
  flex-direction: column;
}
.stat-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.5rem;
}
h3 {
  margin: 0;
  font-size: 1rem;
  color: #6b7280;
  font-weight: 500;
}
.icon {
    font-size: 1.2rem;
}
.stat-value {
  font-size: 2.25rem;
  font-weight: 700;
  color: #111827;
}
.unit {
  font-size: 1rem;
  color: #9ca3af;
  font-weight: 500;
}
</style>
