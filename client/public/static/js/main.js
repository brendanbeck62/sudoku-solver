
var app = new Vue({
  el: '#app',
  data: {
    board: [[]]
  },
  methods: {
    getBoard() {
      const path = 'http://localhost:5000/board';
      axios
        .get(path)
        .then((res) => {
          this.board = res.data.board;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getBoard();
  }
})