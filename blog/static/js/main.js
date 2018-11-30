$(document).ready(() => {
  $(".toggle").on("click", e => {
    e.preventDefault();
    $(".toggle").toggleClass("open");
    $(".menu").toggleClass("active");
  });
  $(".error__close").on("click", () => {
    $(".error").addClass("hidden");
  });
  $('.toggle').on('mouseenter',()=>{
    $('.toggle').addClass('hovered');
  })
  $('.toggle').on('mouseleave', () => {
    $('.toggle').removeClass('hovered');
  })
});
