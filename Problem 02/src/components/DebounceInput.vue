<script>
export default {
  data() {
    return {
      inputNumber: 0,
      msg: 'Project Waste Not',
      saved: false,
      autosaving: false
    }
  },
  methods: {
    valueChanged() {
      this.saved = false
      this.autosaving = true
      setTimeout(() => {
        this.autosaving = false
        this.saved = true

        setTimeout(() => {
          this.saved = false
        }, 2000)

        console.log('Server call that takes 1 second.')
      }, 1000)
    }
  },
  setup() {
    function createDebounce() {
      let timeout = null
      return (callback) => {
        clearTimeout(timeout)
        timeout = setTimeout(() => {
          callback()
        }, 2000)
      }
    }

    return {
      debounce: createDebounce()
    }
  }
}
</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3>
      Place your order quantity:
      <input
        type="number"
        min="0"
        max="999"
        @input="debounce(() => { valueChanged() })"
        v-model="inputNumber"
      >
    </h3>

    <div class="saving-tag" v-if="autosaving">
      Auto-Saving
    </div>

    <div class="saving-tag" v-if="saved">
      Saved
    </div>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.saving-tag {
  background: lightblue;
  padding: 10px;
  color: #f9f9f9;
  max-width: 500px;
  width: 100%;
}
.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
