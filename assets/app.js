(function(){
document.documentElement.className+=' js';
var h=document.getElementById('ham'),m=document.getElementById('menu');
if(h&&m){h.addEventListener('click',function(){var a=m.classList.toggle('acik');
h.setAttribute('aria-expanded',a);h.setAttribute('aria-label',a?'Menüyü kapat':'Menüyü aç');});
m.addEventListener('click',function(e){if(e.target.tagName==='A')m.classList.remove('acik');});}
// video: tıklanana kadar tek bayt inmez
document.querySelectorAll('.video-kutu').forEach(function(kutu){
 var d=kutu.querySelector('.oynat');if(!d)return;
 d.addEventListener('click',function(){
  var v=document.createElement('video');
  v.src=kutu.dataset.video;v.controls=true;v.autoplay=true;v.playsInline=true;v.preload='auto';
  v.style.width='100%';v.style.height='100%';v.style.objectFit='cover';
  kutu.innerHTML='';kutu.appendChild(v);
 });
});
// alt bilgi görünürken yüzen kart çekilsin — footer linklerini örtmesin
var yz=document.querySelector('.yuzen'),ab=document.querySelector('.alt-bilgi');
if(yz&&ab&&'IntersectionObserver'in window){
 new IntersectionObserver(function(ls){
  yz.classList.toggle('gizli',ls[0].isIntersecting);
 },{threshold:0}).observe(ab);
}
// ortaya çıkış — uzun bloklara verilmiyor
if('IntersectionObserver'in window){
 var g=new IntersectionObserver(function(ls){ls.forEach(function(l){
  if(l.isIntersecting){l.target.classList.add('gorundu');g.unobserve(l.target);}});},
  {rootMargin:'0px 0px -60px 0px'});
 document.querySelectorAll('.gel').forEach(function(el,i){
  el.style.transitionDelay=(i%4*60)+'ms';g.observe(el);});
 setTimeout(function(){document.querySelectorAll('.gel:not(.gorundu)').forEach(function(el){
  if(el.getBoundingClientRect().top<innerHeight)el.classList.add('gorundu');});},2500);
}
})();