(()=>{$(document).on("form-refresh",function(o,e){console.log("FROM STREAM PC"),frappe.meta.has_field(e.doc.doctype,"set_posting_time")&&e.is_new()&&(console.log("--------has field-----------"),setTimeout(()=>{e.doc.set_posting_time=1,e.refresh_field("set_posting_time")},500))});})();
//# sourceMappingURL=edit_posting.bundle.DFDLGOYF.js.map
