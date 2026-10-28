(function(){
 const form=document.getElementById('solar-form');
 if(form){
  const byId=id=>document.getElementById(id);
  function calculate(e){if(e)e.preventDefault();
   const bill=Math.max(0,Number(byId('bill').value)||0), tariff=Math.max(1,Number(byId('tariff').value)||8), sun=Math.max(1,Math.min(8,Number(byId('sun').value)||4.5)), area=Math.max(0,Number(byId('area').value)||0);
   const monthlyUnits=bill/tariff, requiredKw=monthlyUnits/(sun*30), areaKw=area/60, kw=Math.max(0,Math.min(requiredKw,areaKw));
   const generation=kw*sun*30, savings=Math.min(bill,generation*tariff*0.85), panels=Math.ceil(kw/0.55), roof=Math.ceil(kw*60);
   byId('system-size').textContent=kw.toFixed(1);byId('generation').textContent=Math.round(generation).toLocaleString('en-IN');byId('savings').textContent=Math.round(savings).toLocaleString('en-IN');byId('annual').textContent=Math.round(savings*12).toLocaleString('en-IN');byId('roof').textContent=roof.toLocaleString('en-IN');byId('panel-note').textContent=kw>0?'About '+panels+' panels at 550 W each; actual design may differ.':'Enter a bill and usable roof area above zero to estimate a system.';
  }
  form.addEventListener('submit',calculate);['bill','tariff','sun','area'].forEach(id=>byId(id).addEventListener('input',calculate));calculate();
 }
})();
