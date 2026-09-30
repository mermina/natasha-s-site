// Rails: mouse wheel scrolls sideways while the pointer is over a rail; arrows; swipe works natively.
document.querySelectorAll('.railbox').forEach(function(box){
  var rail=box.querySelector('.rail'), prev=box.querySelector('.prev'), next=box.querySelector('.next');
  function upd(){ if(!prev) return;
    prev.disabled = rail.scrollLeft<=2;
    next.disabled = rail.scrollLeft+rail.clientWidth>=rail.scrollWidth-2; }
  rail.addEventListener('wheel',function(e){
    if(Math.abs(e.deltaY)<=Math.abs(e.deltaX)) return;          // trackpad sideways: native
    var atStart=rail.scrollLeft<=0, atEnd=rail.scrollLeft+rail.clientWidth>=rail.scrollWidth-1;
    if((e.deltaY<0&&atStart)||(e.deltaY>0&&atEnd)) return;      // at an end: let the page scroll
    e.preventDefault(); rail.scrollLeft+=e.deltaY;
  },{passive:false});
  function go(d){ rail.scrollBy({left:d*rail.clientWidth*0.8,behavior:'smooth'}); }
  if(prev){ prev.onclick=function(){go(-1)}; next.onclick=function(){go(1)}; }
  rail.addEventListener('scroll',upd); window.addEventListener('resize',upd); window.addEventListener('load',upd); upd();
});
// Missing book cover -> typographic card
function ph(img){ var f=img.closest('figure'); var d=document.createElement('div'); d.className='ph';
  d.textContent=f?f.getAttribute('data-title'):''; img.replaceWith(d); }
// Lightbox
function lb(fig){ if(!fig.querySelector('img')) return;
  document.getElementById('lb-img').src=fig.getAttribute('data-big');
  document.getElementById('lb-title').textContent=fig.getAttribute('data-title')||'';
  document.getElementById('lb-meta').textContent=fig.getAttribute('data-meta')||'';
  document.getElementById('lb').classList.add('on'); }
document.addEventListener('keydown',function(e){ if(e.key==='Escape'){var l=document.getElementById('lb'); if(l) l.classList.remove('on');} });
