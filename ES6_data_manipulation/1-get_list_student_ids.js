const getListStudentIds = (list) => {
    if (!Array.isArray(list)) return [];
    return list.map((l) => l.id);
  };
  
  export default getListStudentIds;
  