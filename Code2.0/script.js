


Vue.config.devtools = true;

Vue.component('cardz', {
  template: `
    <div class="cardz-wrap"
      @mousemove="handleMouseMove"
      @mouseenter="handleMouseEnter"
      @mouseleave="handleMouseLeave"
      ref="cardz">
      <div class="cardz"
        :style="cardzStyle">
        <div class="cardz-bg" :style="[cardzBgTransform, cardzBgImage]"></div>
        <div class="cardz-info">
          <slot name="header"></slot>
          <slot name="content"></slot>
        </div>
      </div>
    </div>`,
  mounted() {
    this.width = this.$refs.cardz.offsetWidth;
    this.height = this.$refs.cardz.offsetHeight;
  },
  props: ['dataImage'],
  data: () => ({
    width: 0,
    height: 0,
    mouseX: 0,
    mouseY: 0,
    mouseLeaveDelay: null }),

  computed: {
    mousePX() {
      return this.mouseX / this.width;
    },
    mousePY() {
      return this.mouseY / this.height;
    },
    cardzStyle() {
      const rX = this.mousePX * 30;
      const rY = this.mousePY * 3;
      return {
        transform: `rotateY(${rX}deg) rotateX(${rY}deg)` };

    },
    cardzBgTransform() {
      const tX = this.mousePX * 40;
      const tY = this.mousePY * -4;
      return {
        transform: `translateX(${tX}px) translateY(${tY}px)` };

    },
    cardzBgImage() {
      return {
        backgroundImage: `url(${this.dataImage})` };

    } },

  methods: {
    handleMouseMove(e) {
      this.mouseX = e.pageX - this.$refs.cardz.offsetLeft - this.width / 2;
      this.mouseY = e.pageY - this.$refs.cardz.offsetTop - this.height / 2;
    },
    handleMouseEnter() {
      clearTimeout(this.mouseLeaveDelay);
    },
    handleMouseLeave() {
      this.mouseLeaveDelay = setTimeout(() => {
        this.mouseX = 0;
        this.mouseY = 0;
      }, 1000);
    } } });



const app = new Vue({
  el: '#appz' });